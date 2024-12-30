import time
import os
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
        self.state = "to-do"
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
        print(f"Task {new_id} created successfully.")
    
    def mark_task(self, id, state):
        """ Mark a task as: In progress, Todo or Done. """
        pass




def handle_add_task(args):
    task = Task(args.task)
    task.create_task()

def handle_mark_tasks(args):
    tasks = Task.load_tasks()
    print(tasks)
    print(type(tasks))

def main():
    parser =  argparse.ArgumentParser(prog="task-cli")
    subparser = parser.add_subparsers(help='subcommand help')
    
    # Add Subcommand
    parser_add = subparser.add_parser('add', help="add a task to the list")
    parser_add.add_argument('task', help="Name of the task")
    parser_add.set_defaults(func=handle_add_task)
    
    # Mark Subcommand
    parser_mark = subparser.add_parser('mark', help="mark a task as: 'to-do, in-progress or done.'")
    parser_mark.add_argument('id', help="ID of the task to mark.", type=int)
    parser_mark.add_argument("state", choices=["to-do", "in-progress", "done"], type=str)
    parser_mark.set_defaults(func=handle_mark_tasks)
    
    # Parse Args
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":    
    main()