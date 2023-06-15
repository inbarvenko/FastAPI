from db.schemas import toDoListEntity
import math
from db.connection import collection

class ToDoControllers:
    def find_with_filer_and_pagination(filter='all', currentPage = 1):
      try:
        if (filter == 'all' or not filter):
          filteredObject = {}
        else:
          filteredObject = { 'completed': filter == 'completed' }

        todosForPage = 10

        todos = toDoListEntity(collection
                               .find(filteredObject)
                               .skip((currentPage - 1)*todosForPage)
                               .limit(todosForPage))
        activeTasks = collection.count_documents({'completed': False})
        filteredItems = collection.count_documents(filteredObject)

        allPages = math.ceil(filteredItems // todosForPage)
        pages = [i+1 for i in range(allPages + 1)]
                                
        return {"todos": todos,
                "pages": pages, 
                "activeTasks": activeTasks}
      except:
        print("Something went wrong")

