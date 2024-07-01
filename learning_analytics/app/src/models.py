import uuid

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.database import Base


class Student(Base):
    __tablename__ = "students"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=True)
    messages = relationship("Message", back_populates="student")


class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    response = Column(String)
    student_id = Column(UUID(as_uuid=True), ForeignKey("students.id"))
    student = relationship("Student", back_populates="messages")
