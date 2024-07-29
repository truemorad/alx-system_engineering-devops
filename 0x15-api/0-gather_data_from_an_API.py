#!/usr/bin/python3
"""This script fetches the TODO list progress of an employee."""

import requests
import sys

if __name__ == "__main__":
    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId))
    name = user.json()

    EMPLOYEE_NAME = name.get('name')

    todos_url = requests.get('https://jsonplaceholder.typicode.com/todos')
    if todos_url.status_code == 200:
        todos = todos_url.json()

    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0

    for task in todos:
        if task.get('userId') == int(userId):
            TOTAL_NUMBER_OF_TASKS += 1
            if task.get('completed'):
                NUMBER_OF_DONE_TASKS += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

    print('\n'.join(["\t " + task.get('title') for task in todos
          if task.get('userId') == int(userId) and task.get('completed')]))
