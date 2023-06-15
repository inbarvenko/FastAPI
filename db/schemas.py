def toDoEntity(item) -> dict:
  return {
    "_id": str(item["_id"]),
    "title": item["title"],
    "completed": item["completed"],
  }

def toDoListEntity(entity) -> list:
  return [toDoEntity(item) for item in entity]