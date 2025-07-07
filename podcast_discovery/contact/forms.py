import reflex as rx
from pydantic import ValidationError

from podcast_discovery.contact.models import ContactMessageModel
from podcast_discovery.contact.schemas import ContactMessageCreateSchema
from podcast_discovery.providers.clerk_provider import reclerk

class ContactFormState(rx.State):
    form_data: dict = {}
    errors: dict = {}
    message: dict = {}
    has_errors: bool = False

    def reset_form(self):
        self.has_errors = False
        self.errors = {}
        self.form_data = {}

    @rx.event
    def handle_reset_button(self):
        self.reset_form()
        self.message = {}

    @rx.event
    async def handle_form_submit(self, form_data: dict):
        self.form_data = form_data
        clerk_state = await self.get_state(reclerk.ClerkState)
        # clerk_user = await self.get_state(reclerk.ClerkUser)
        print(clerk_state.user_id)
        user_id = rx.cond(reclerk.ClerkState.user_id, reclerk.ClerkState.user_id, "")
        with rx.session() as session:
            try:
                model_data = ContactMessageCreateSchema.model_validate(form_data)
            except ValidationError as e:
                for err in e.errors():
                    field_name = err["loc"][0] if err["loc"] else "general"
                    self.errors[field_name] = err["msg"]
                self.has_errors = True
                return
            except Exception as e:
                self.has_errors = True
                self.errors = {
                    "general": f"An error occured: {str(e)}"
                }
                return

            # storing to db as is
            instance = ContactMessageModel(**model_data.model_dump())
            if clerk_state.user_id:
                instance.user_id = clerk_state.user_id

            session.add(instance)
            session.commit()
            session.refresh(instance)
            self.reset_form()
            self.message = instance.model_dump()


def contact_form() -> rx.Component:
    init_name_val = rx.cond(
        ContactFormState.form_data.get("name"),
        ContactFormState.form_data.get("name"),
        ""
    )
    init_message_val = rx.cond(
        ContactFormState.form_data.get("message"),
        ContactFormState.form_data.get("message"),
        ""
    )

    return rx.vstack(
        rx.cond(
            ContactFormState.has_errors,
            rx.text("There was a validation error. Please try again.", color="red"),
            None),
        rx.form(
            rx.vstack(
                rx.input(
                    placeholder="Your name",
                    default_value=init_name_val,
                    name="name",
                    type="text",
                ),
                rx.text_area(
                    placeholder="Your message",
                    name="message",
                ),
                rx.hstack(
                    rx.button(
                        "Send message",
                        type="submit",
                    ),
                    rx.button(
                        "Reset",
                        on_click=ContactFormState.handle_reset_button,
                    ),
                ),
            ),
            on_submit=ContactFormState.handle_form_submit,
            reset_on_submit=True,
        ),
        rx.divider(),
        rx.heading("Input value"),
        rx.text(ContactFormState.message)
    )
