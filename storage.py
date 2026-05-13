import json
import os

from task import Task

class Storage:
    #contructor
    def __init__(self, filename="data.json"):
        self.filename = filename
    
    def save_tasks(self, tasks):
        #list chứa dict
        data = []

        for task in tasks:
            data.append(task.to_dict())

        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def load_tasks(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        tasks = []

        for item in data:

            task = Task(
                item["id"],
                item["title"],
                item.get("completed", False)
            )

            tasks.append(task)

        return tasks