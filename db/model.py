from pydantic import BaseModel


# Model of request
class ToDoListModel(BaseModel):
    _id: str
    title: str
    completed: bool