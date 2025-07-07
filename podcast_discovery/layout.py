import reflex as rx
from podcast_discovery.ui.nav import navbar
from podcast_discovery.providers.clerk_provider import my_clerk_provider


def root_layout(child: rx.Component, *args, **kwargs) -> rx.Component:
    return my_clerk_provider(
        rx.container(
            navbar(),
            rx.fragment(child),
            rx.logo(),
            width="100%",
            id="my-root-layout",
            *args,
            **kwargs,
        )
    )
