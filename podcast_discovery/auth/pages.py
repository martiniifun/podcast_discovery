import reflex as rx
import reflex_clerk_api as reclerk
from podcast_discovery.layout import root_layout


@rx.page(route="/login")
def login_page() -> rx.Component:
    return root_layout(
        rx.center(
            reclerk.sign_in(),
            min_height="85vh",
        )
    )


@rx.page(route="/signup")
def signup_page() -> rx.Component:
    return root_layout(
        rx.center(
            reclerk.sign_up(),
            min_height="85vh",
        )
    )


@rx.page(route="/logout")
def logout_page() -> rx.Component:
    return root_layout(
        rx.center(
            rx.vstack(
                rx.heading(
                    "Are you sure you want to logout?"
                ),
                rx.hstack(
                    reclerk.sign_out_button(rx.button("Yes, logout!")),
                    rx.link(rx.button("No, cancel!", variant="outline"), href="/")
                )
            ),
            min_height="85vh",
        )
    )