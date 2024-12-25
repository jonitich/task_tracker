import time
import os
import io
from pathlib import Path
import json
import argparse

class Task():
    """ This class is a template for Tasks objects """
    
    FILE_PATH = "./tasks.json"
    
    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, "w") as f:
            json.dump([], f)
    
    def __init__(self, task):
        self.description = task
        self.state = "todo"
        self.creation_at = time.ctime()
        self.update_at = time.ctime()
    
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
            "description": self.description,
            "status": self.state,
            "createdAt": self.creation_at,
            "updatedAt": self.update_at
        }
        tasks.append(task)
        self.save_tasks(tasks)
    
    def mark_task(self, id):
        """ Mark a task as: In progress, Todo or Done. """
        

def handle_task(args):
    task = Task(args.task)
    task.create_task()


def main():
    parser =  argparse.ArgumentParser(prog="task-cli")
    subparser = parser.add_subparsers(help='subcommand help')
    
    # Add subcommand
    parser_add = subparser.add_parser('add', help="add a task to the list")
    parser_add.add_argument('task', help="Name of the task")
    args = parser.parse_args()
    handle_task(args)

if __name__ == "__main__":    
    main()