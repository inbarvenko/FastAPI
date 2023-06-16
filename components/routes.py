from pymongo import MongoClient
import os
from fastapi import APIRouter
from db.schemas import toDoListEntity, toDoEntity
from db.model import ToDoListModel
from bson import ObjectId
from components.controllers import ToDoControllers
from db.connection import collection
from components.req_models import req_add, req_id, data

todo = APIRouter()

@todo.get('/')
async def find_all_todos(filter: str, currentPage: int):
    return ToDoControllers.find_with_filer_and_pagination(filter, currentPage)

@todo.post('/')
async def create_todo(data:req_add):
    print(data.title)
    todo = {
        "title":data.title,
        "completed": False
    }
    collection.insert_one(dict(todo))
    return toDoListEntity(collection.find())

@todo.delete('/')
async def delete_user(obj:req_id):
    return toDoEntity(collection.find_one_and_delete({"_id": ObjectId(obj.id)}))

@todo.put("/")
async def update_item(obj:data):
    print(obj.item)
    collection.find_one_and_update({"_id": ObjectId(obj.item.id)},{
        "$set":dict({
            'title': obj.item.title,
            'completed': obj.item.completed
            })
    })
    return toDoEntity(collection.find_one({"_id": ObjectId(obj.item.id)}))
