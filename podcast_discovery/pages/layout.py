import reflex as rx
from podcast_discovery import ui
from podcast_discovery.layout import root_layout
from podcast_discovery.ui.nav import navbar


def page_layout(children: rx.Component, title: str = "Page", *args, **kwargs) -> rx.Component:
    return root_layout(
        rx.container(
            rx.color_mode.button(position="top-right"),
            rx.vstack(
                ui.page_heading(title),
                rx.box(
                    children
                ),
                rx.link(
                    rx.button("home"),
                    href="/",
                    is_external=False,
                ),
                rx.link(
                    rx.button("contact"),
                    href="/contact",
                    is_external=False,
                ),
                rx.link(
                    rx.button("about"),
                    href="/about",
                    is_external=False,
                ),
                spacing="5",
                justify="center",
                min_height="85vh",
            )
        )
    )
