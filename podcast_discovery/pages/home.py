import reflex as rx
from podcast_discovery.pages.layout import page_layout
from podcast_discovery.layout import root_layout
from podcast_discovery.states.State import State


@rx.page(route="/")
def index_page() -> rx.Component:
    return root_layout(
        rx.container(
            rx.vstack(
                rx.heading(State.title, size="9"),
                rx.button("Click me", on_click=State.handle_click_event),
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        )
    )