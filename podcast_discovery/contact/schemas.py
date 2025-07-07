from pydantic import BaseModel, field_validator


class ContactMessageCreateSchema(BaseModel):
    name: str
    message: str

    @field_validator('name')
    @classmethod
    def validate_name(cls, val):
        if "justin" in val.lower():
            raise ValueError("Name cannot contain 'Justin'")
        return val