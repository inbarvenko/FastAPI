from pydantic import BaseModel


# Model of request
class toDoListModel(BaseModel):
    title: str
    completed: bool