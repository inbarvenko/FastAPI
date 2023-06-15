from pymongo import MongoClient

connection = MongoClient('mongodb+srv://inbarvenko:Llola2002@todo.ny1ljjp.mongodb.net/?retryWrites=true&w=majority')
collection = connection.ToDoList.todos