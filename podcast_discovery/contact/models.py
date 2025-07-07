import reflex as rx
from sqlmodel import Field
import sqlalchemy
from datetime import datetime, timezone
from .schemas import ContactMessageCreateSchema

# oauth login -> google login, meta/facebook, x login, github login
# handle callback url
# SSO -> login
# MFA -> sms text (Multi Factor Authentication)
# Phone-number based login
# HIPAA


class ContactMessageModel(rx.Model, table=True):
    name: str
    message: str
    user_id: str | None = Field(default=None, index=True)
    created_at: datetime = Field(
        default_factory=datetime.now,
        sa_type=sqlalchemy.DateTime(timezone=False),
        sa_column_kwargs={'server_default': sqlalchemy.func.now()},
        nullable=False,
    )
