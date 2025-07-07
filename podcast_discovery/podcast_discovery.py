import reflex as rx
import reflex_clerk_api as reclerk

from .pages import *
from .contact import *
from .layout import root_layout
from podcast_discovery.auth.pages import login_page
from podcast_discovery.providers.clerk_provider import my_clerk_provider_args

app = rx.App()
# reclerk.wrap_app(app, **my_clerk_provider_args)