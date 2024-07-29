#!/usr/bin/python3
"""This script export TODO list."""
import json
import requests
import sys

if __name__ == "__main__":
    user = requests.get("https://jsonplaceholder.typicode.com/users")
    users = user.json()
    todos_url = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos_url.json()
    
    todolist = {}

    for user in users:
        tasklist = []
        for task in todos:
            if task.get('userId') == user.get('id'):
                taskDict = {"username": user.get('username'),
                            "task": task.get('title'),
                            "completed": task.get('completed')}
                tasklist.append(taskDict)
        todolist[user.get('id')] = tasklist

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(todolist, f)

