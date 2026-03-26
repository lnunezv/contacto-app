from pydantic import BaseModel, EmailStr
from datetime import datetime


class ContactBase(BaseModel):
    name: str
    email: EmailStr
    subject: str
    message: str


class ContactCreate(ContactBase):
    pass


class ContactResponse(ContactBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True