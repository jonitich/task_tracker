import argparse
import json

class Task():
    def __init__(self, id, description, status, created_at, updataed_at):
        self.id = id
        self.description = description
        self.status = status
        self.created_at = created_at
        self.updated_at = updataed_at
    
    def setter(self):
        pass
    
    def add_task(self):
        pass
    
    def update_task():
        pass
    
    def delete_task():
        pass

def main(action, task):
    match action:
        case "add":
            t = Task()
            add_task(task)
        case _:
            print("Another action was supplied")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="task", description="This programme \
        is a task manager.")
    parser.add_argument("action", choices=["add","update", "delete"])
    parser.add_argument("task", help="Task to add to the list.")
    args = parser.parse_args()
    # parser.print_help()
    main(args.action, args.task)