import os
from fastapi import FastAPI
import motor.motor_asyncio
from pydantic import BaseModel, Field
from typing import List
from bson import ObjectId


app = FastAPI()
client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv("MONGODB_URL"))
db = client.college

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


# Model of request
class toDoListModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    title: str = Field(...)
    completed: bool = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


@app.get(
    "/", response_description="List todos", response_model=List[toDoListModel]
)
def list_todos():
    todos = db["todo"].find()
    return todos
