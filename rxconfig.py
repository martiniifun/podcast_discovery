import reflex as rx
import os
from dotenv import load_dotenv


load_dotenv()
DATABASE_URL = os.environ.get("DATABASE_URL")

config = rx.Config(
    app_name="podcast_discovery",
    db_url=DATABASE_URL,
    plugins=[],
)
