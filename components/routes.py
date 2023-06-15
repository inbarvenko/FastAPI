from pymongo import MongoClient
import os
from fastapi import APIRouter
from db.schemas import toDoListEntity, toDoEntity
from db.model import toDoListModel
from bson import ObjectId

# print(os.environ.get('MONGODB_URL'))
# MONGODB_URL = 'mongodb+srv://inbarvenko:Llola2002@todo.ny1ljjp.mongodb.net/?retryWrites=true&w=majority'
connection = MongoClient('mongodb+srv://inbarvenko:Llola2002@todo.ny1ljjp.mongodb.net/?retryWrites=true&w=majority')
db = connection.ToDoList
collection = db.todos

todo = APIRouter()

@todo.get('/')
async def find_all_todos():
    try:
        print(toDoListEntity(collection.find()))
        return toDoListEntity(collection.find())
    except:
        print("Something went wrong")

@todo.post('/')
async def create_todo(todo: toDoListModel):
    collection.insert_one(dict(todo))
    return toDoListEntity(collection.find())

@todo.delete('/')
async def delete_user(item_id):
    return toDoEntity(collection.find_one_and_delete({"_id": ObjectId(item_id)}))

@todo.patch("/")
async def update_item(item_id, item: toDoListModel):
    collection.find_one_and_update({"_id": ObjectId(item_id)},{
        "$set":dict(item)
    })
    return toDoEntity(collection.find_one({"_id": ObjectId(item_id)}))
