import os
import reflex as rx
import reflex_clerk_api as reclerk
from dotenv import load_dotenv

load_dotenv("../../.env.dev")


def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium"), href=url
    )


def mobile_navbar_link(url: str):
    return rx.redirect(url)


def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/64px.png",
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Podcast Discovery", size="7", weight="bold",
                        on_click=lambda: rx.redirect("/"),
                    ),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_link("Home", "/"),
                    navbar_link("About", "/about"),
                    navbar_link("Pricing", "/pricing"),
                    navbar_link("Contact", "/contact"),
                    rx.fragment(
                        reclerk.signed_out(
                            reclerk.sign_in_button(rx.button("Sign in", variant="outline")),
                            reclerk.sign_up_button(rx.button("Sign up")),
                        ),
                    ),
                    rx.fragment(
                        reclerk.signed_in(
                            reclerk.sign_out_button(rx.button("Log out")),
                        ),
                    ),
                    justify="end",
                    spacing="3",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/64px.png",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Reflex", size="6", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item("Home", on_click=mobile_navbar_link("/")),
                        rx.menu.item("About", on_click=mobile_navbar_link("/about")),
                        rx.menu.item("Pricing", on_click=mobile_navbar_link("/pricing")),
                        rx.menu.item("Contact", on_click=mobile_navbar_link("/contact")),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
    )
