import os, json, time

class Task():
    """ This class is a template for Tasks objects """
    
    FILE_PATH = f"{os.getenv('HOME')}/github/task_tracker/tasks.json"
    
    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, "w") as f:
            json.dump([], f)
    
    def __init__(self, task, notes=""):
        self.task = task
        self.state = "to-do"
        self.creation_at = time.ctime()
        self.update_at = time.ctime()
        self.notes = notes
    
    @staticmethod
    def load_tasks():
        """ Load tasks """
        with open(Task.FILE_PATH,"r") as f:
            return json.load(f)
    
    @staticmethod
    def save_tasks(tasks):
        with open(Task.FILE_PATH, "w") as f:
            json.dump(tasks, f)
    
    def create_task(self):
        """ Cretate task method """
        tasks = self.load_tasks()
        new_id = max([task["id"] for task in tasks], default=0) + 1
        task = {
            "id": new_id,
            "title": self.task,
            "status": self.state,
            "createdAt": self.creation_at,
            "updatedAt": self.update_at,
            "notes": self.notes
        }
        tasks.append(task)
        self.save_tasks(tasks)
        print(f"Task {new_id} created successfully.")