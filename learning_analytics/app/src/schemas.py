from typing import Optional
from pydantic import BaseModel, EmailStr
from uuid import UUID


class MessageBase(BaseModel):
    content: str
    response: str


class MessageCreate(MessageBase):
    pass


class Message(MessageBase):
    id: int
    student_id: UUID

    class Config:
        orm_mode = True


class StudentBase(BaseModel):
    name: str
    email: Optional[EmailStr] = None


class StudentCreate(StudentBase):
    pass


class Student(StudentBase):
    id: UUID
    messages: list[Message] = []

    class Config:
        orm_mode = True


class StudentUpdate(StudentBase):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
