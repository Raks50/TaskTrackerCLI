import json
import sys
import os

tasks_file = tasks.json

# Function to add new task 
def add_task(task_description):
    task = {
        "Task": task_description, "Completed": False
    }
    with open(tasks_file, "a") as file:
        json.dump(tasks, file)
        file.write("\n")

