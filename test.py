from fastapi import FastAPI
from components.routes import todo

app = FastAPI()
app.include_router(todo)