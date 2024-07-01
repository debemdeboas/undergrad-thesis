import os
import uuid

import httpx
import src.errors as errors
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from src import models, schemas
from src.database import SessionLocal, engine
import json

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def generate_topics_via_api(content: str, msg_response: str) -> list[str]:
    async with httpx.AsyncClient() as client:
        response = await client.post(
            os.getenv("OLLAMA_BASE_URL", "") + "/api/generate",
            json={
                "model": "llama3:70b-instruct",
                "system": "Extract topics in portuguese from the following message and its response. If there are no topics, respond with an empty list []. Respond using only JSON. Example response: \"{'topics': ['Algoritmos']}\".",
                "prompt": (f'Message: "{content}". Response: "{msg_response}".'),
                "format": "json",
                "stream": False,
            },
            timeout=999,
        )
        response.raise_for_status()
        print(response)
        topics = json.loads(response.json().get("response", {})).get("topics", [])
    return topics


@app.post("/api/", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    db_student = models.Student(name=student.name, email=student.email)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


@app.get("/api/", response_model=list[schemas.Student])
def read_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    students = db.query(models.Student).offset(skip).limit(limit).all()
    return students


@app.get("/api/{student_id}", response_model=schemas.Student)
def read_student(student_id: uuid.UUID, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail=errors.STUDENT_NOT_FOUND)
    return student


@app.put("/api/{student_id}", response_model=schemas.Student)
def update_student(student_id: uuid.UUID, updated_student: schemas.StudentCreate, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail=errors.STUDENT_NOT_FOUND)
    student.name = updated_student.name
    student.email = updated_student.email
    db.commit()
    db.refresh(student)
    return student


@app.delete("/api/{student_id}")
def delete_student(student_id: uuid.UUID, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail=errors.STUDENT_NOT_FOUND)
    db.delete(student)
    db.commit()
    return {"message": "Student deleted successfully"}


@app.post("/api/{student_id}/messages/", response_model=schemas.Message)
def create_message_for_student(student_id: uuid.UUID, message: schemas.MessageCreate, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail=errors.STUDENT_NOT_FOUND)
    db_message = models.Message(content=message.content, response=message.response, student_id=student_id)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message


@app.get("/api/{student_id}/messages/", response_model=list[schemas.Message])
def read_messages(student_id: uuid.UUID, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    messages = db.query(models.Message).filter(models.Message.student_id == student_id).offset(skip).limit(limit).all()
    return messages


@app.patch("/api/{student_id}", response_model=schemas.Student)
def student_create_if_not_exists(
    student_id: uuid.UUID, updated_student: schemas.StudentUpdate, db: Session = Depends(get_db)
):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()

    if student is None:
        student = models.Student(id=student_id, name=updated_student.name, email=updated_student.email)
        db.add(student)
    else:
        for key, value in updated_student.model_dump(exclude_unset=True).items():
            # Check if the key is a valid attribute of the student model
            if not hasattr(student, key):
                continue

            # Check if the attrs are different
            if getattr(student, key) == value:
                continue

            setattr(student, key, value)

    db.commit()
    db.refresh(student)
    return student


@app.get("/api/{student_id}/generate_topics")
async def generate_topics_for_student(student_id: uuid.UUID, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    messages = db.query(models.Message).filter(models.Message.student_id == student_id).all()

    topics = []
    for message in messages:
        topics.extend(await generate_topics_via_api(message.content, message.response))

    return topics
