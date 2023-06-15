from pymongo import MongoClient
import os
from fastapi import APIRouter
from db.schemas import toDoListEntity, toDoEntity
from db.model import toDoListModel
from bson import ObjectId
from components.controllers import ToDoControllers
from db.connection import collection

todo = APIRouter()

@todo.get('/')
async def find_all_todos(filter: str, currentPage: int):
    return ToDoControllers.find_with_filer_and_pagination(filter, currentPage)

@todo.post('/')
async def create_todo(title: str):
    print(title)
    todo = {
        "title":title,
        "completed": False
    }
    collection.insert_one(dict(todo))
    return toDoListEntity(collection.find())

@todo.delete('/')
async def delete_user(item_id):
    print(item_id)
    return toDoEntity(collection.find_one_and_delete({"_id": ObjectId(item_id)}))

@todo.put("/")
async def update_item(item_id, item: toDoListModel):
    collection.find_one_and_update({"_id": ObjectId(item_id)},{
        "$set":dict(item)
    })
    return toDoEntity(collection.find_one({"_id": ObjectId(item_id)}))
