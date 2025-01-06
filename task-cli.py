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


def handle_add_task(args):
    task = Task(args.task)
    task.create_task()

def handle_mark_tasks(args):
    tasks = Task.load_tasks()
    for task in tasks:
        if task["id"] == args.id:
            t = {
                "id": args.id,
                "description": task["description"],
                "status": args.state,
                "createdAt": task["createdAt"],
                "updatedAt": time.ctime()
            }
            tasks[args.id -1] = t
            Task.save_tasks(tasks)

def handle_list_tasks(args):
    tasks = Task.load_tasks()
    match args.task:
        case "all":
            for task in tasks:
                print(task)
        case "to-do":
            for task in tasks:
                if task["status"] == "to-do":
                    print(task)
        case "in-progress":
            for task in tasks:
                if task["status"] == "in-progress":
                    print(task)
        case "done":
            for task in tasks:
                if task["status"] == "done":
                    print(task)

def handle_delete_task(args):
    tasks = Task.load_tasks()
    new_task_list = []
    for i in range(len(tasks)):
        if tasks[i]["id"] == args.id:
            continue
        new_task_list.append(tasks[i])
    Task.save_tasks(new_task_list)

def handle_update_task(args):
    tasks = Task.load_tasks()
    for task in tasks:
        if task["id"] == args.id:
            task["description"] = args.description
            Task.save_tasks(tasks)

def main():
    parser =  argparse.ArgumentParser(prog="task-cli")
    subparser = parser.add_subparsers(help='subcommand help')
    
    # Add Subcommand
    parser_add = subparser.add_parser('add', help="add a task to the list.")
    parser_add.add_argument('task', help="Name of the task.")
    parser_add.set_defaults(func=handle_add_task)
    
    # Mark Subcommand
    parser_mark = subparser.add_parser('mark', help="mark a task as: 'to-do, in-progress or done.'")
    parser_mark.add_argument('id', help="ID of the task to mark.", type=int)
    parser_mark.add_argument("state", choices=["to-do", "in-progress", "done"], type=str)
    parser_mark.set_defaults(func=handle_mark_tasks)
    
    # List Subcommand
    parser_list = subparser.add_parser("list", help="List tasks.")
    parser_list.add_argument("task", choices=["all", "to-do", "in-progress", "done"])
    parser_list.set_defaults(func=handle_list_tasks)
    
    # Delete Subcommand
    parser_delete = subparser.add_parser("delete", help="Delete a task by its ID.")
    parser_delete.add_argument("id", type=int)
    parser.set_defaults(func=handle_delete_task)
    
    # Update Subcommand
    parser_update = subparser.add_parser("update", help="Update the description of a task.")
    parser_update.add_argument("id", type=int)
    parser_update.add_argument("description", help="The new description of the task.")
    parser_update.set_defaults(func=handle_update_task)
    
    # Parse Args
    args = parser.parse_args()
    try:
        args.func(args)
    except AttributeError:
        print(parser.print_help())

if __name__ == "__main__":    
    main()