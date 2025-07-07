import reflex as rx
from podcast_discovery.pages.layout import page_layout
from podcast_discovery.layout import root_layout
from podcast_discovery.states.State import State
import reflex_clerk_api as reclerk
from reflex_clerk_api import ClerkUser, ClerkState
from podcast_discovery import auth


@rx.page(route="/")
def index_page() -> rx.Component:
    welcome_message = rx.cond(
        ClerkState.is_signed_in,
        rx.hstack(
            rx.text("Welcome, ", ClerkUser.first_name, ClerkUser.last_name),
            rx.image(ClerkUser.image_url, width=100, height=100),
            justify="center",
            align="center",
        ),
        State.title,
    )

    return root_layout(
        rx.container(
            rx.vstack(
                rx.heading(welcome_message, size="9"),
                rx.button("Click me", on_click=State.handle_click_event),
                rx.link(
                    rx.button("Contact us!"),
                    href="/contact",
                    is_external=False,
                ),
                spacing="5",
                justify="center",
                min_height="85vh",
            ),
            size="4",

        ),

    )
