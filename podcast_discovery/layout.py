import reflex as rx

from podcast_discovery.providers import my_clerk_provider_args
from podcast_discovery.ui.nav import navbar
import reflex_clerk_api as reclerk
from podcast_discovery.ui.sidebar import user_sidebar


def non_user_layout(child: rx.Component) -> rx.Component:
    return rx.container(
        navbar(),
        rx.fragment(child),
        width="100%",
        id="my-root-layout",
    )


def user_layout(child: rx.Component) -> rx.Component:
    return rx.box(
        rx.hstack(
            user_sidebar(),
            rx.fragment(child),
        ),
        width="100%",
        id="my-root-layout",
    )


def root_layout(child: rx.Component, *args, **kwargs) -> rx.Component:
    return \
        reclerk.clerk_provider(
            rx.fragment(
                reclerk.clerk_loading(
                    rx.spinner(),
                ),
                reclerk.clerk_loaded(
                    reclerk.signed_in(
                        # reclerk.sign_out_button(),
                        user_layout(child),
                    ),
                    reclerk.signed_out(
                        # reclerk.sign_in_button(),
                        non_user_layout(child),
                    ),
                ),
            ),
            **my_clerk_provider_args
        )
