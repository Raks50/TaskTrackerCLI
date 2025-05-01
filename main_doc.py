import json
import sys
import os

tasks_file = "tasks.json"

# Function to add new task 
def add_task(task_description):
    task = {
        "Task": task_description, "Completed": False
    }
    with open(tasks_file, "a") as file:
        json.dump(task, file)
        file.write("\n")

# Main part of program

# Explanation to user of how to write command to add new task
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python main_doc.py add 'task description'")
    else: 
        command = sys.argv[1] # Command
        task_description = " ".join(sys.argv[2:0]) # Task
        if command == "add":
            add_task(task_description)
            print(f"Task added: {task_description}")
