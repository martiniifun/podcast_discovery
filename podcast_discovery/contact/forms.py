import reflex as rx
from podcast_discovery.contact.models import ContactMessageModel


class ContactFormState(rx.State):
    form_data: dict = {}
    message_id: int|None = None

    @rx.event
    def handle_form_submit(self, form_data: dict):
        self.form_data = form_data
        with rx.session() as session:
            instance = ContactMessageModel.model_validate(form_data)
            session.add(instance)
            session.commit()
            session.refresh(instance)
            self.message_id = instance.id


def contact_form() -> rx.Component:
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.input(
                    placeholder="input your first name",
                    name="name",
                    type="text",
                ),
                rx.text_area(
                    placeholder="Your message",
                    name="message",
                ),
                rx.button(
                    "Send message",
                    type="submit",
                ),

            ),
            on_submit=ContactFormState.handle_form_submit,
            reset_on_submit=True,
        ),
        rx.divider(),
        rx.heading("Input value"),
        rx.text(ContactFormState.message_id.to_string()),
    )
