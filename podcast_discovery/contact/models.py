import reflex as rx
from sqlmodel import Field
import sqlalchemy
from datetime import datetime, timezone


# class ContactMessageCreate(rx.Model):
#     name: str
#     nessage: str


class ContactMessageModel(rx.Model, table=True):
    name: str
    message: str
    user_id: int|None = Field(default=None, nullable=True, index=True)
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_type=sqlalchemy.DateTime(timezone=False),
        sa_column_kwargs={'server_default': sqlalchemy.func.now()},
        nullable=False,
    )