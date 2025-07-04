import reflex as rx


def page_heading(title: str = "Page", color_scheme: str = "teal", *args, **kwargs) -> rx.Component:
    return rx.heading(title, size="9", color_scheme=color_scheme, *args, **kwargs)