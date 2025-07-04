import reflex as rx
from podcast_discovery.pages.layout import page_layout
from .forms import contact_form


@rx.page(route='/contact')
def contact_page() -> rx.Component:
    return page_layout(
        rx.fragment(
            rx.text("This is my contact page. I'll add to it later."),
            contact_form(),
        ),
        title="Contact Page",
    )
