from pydantic import BaseModel

class req_add(BaseModel):
  title: str

  class Config:
        orm_mode = True

class req_id(BaseModel):
  id: str

class req_todo(BaseModel):
  id: str
  title:str
  completed: bool

class data(BaseModel):
   item: req_todo