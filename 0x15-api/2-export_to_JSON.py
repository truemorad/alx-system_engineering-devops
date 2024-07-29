#!/usr/bin/python3
"""This script export TODO list."""
import json
import requests
import sys

if __name__ == "__main__":
    USER_ID = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(USER_ID))

    todos_url = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos_url.json()
    
    todouser = {}
    tasklist = []

    for task in todos:
        if task.get('userId') == int(USER_ID):
            taskDict = {"task": task.get('title'),
                         "completed": task.get('completed'),
                         "username": user.json().get('username')}
            tasklist.append(taskDict)
    todouser[USER_ID] = tasklist

    filename = USER_ID + '.json'
    with open(filename, mode='w') as f:
        json.dump(todouser,f)
