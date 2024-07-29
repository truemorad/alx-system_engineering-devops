#!/usr/bin/python3
"""This script export TODO list."""
import csv
import requests
import sys

if __name__ == "__main__":
    USER_ID = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(USER_ID))
    name = user.json()

    USERNAME = name.get('name')

    todos_url = requests.get('https://jsonplaceholder.typicode.com/todos')
    if todos_url.status_code == 200:
        todos = todos_url.json()

    filename = USER_ID + '.csv'
    with open(filename, mode='w') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL, lineterminator='\n')
        for task in todos:
            if task.get('userId') == int(USER_ID):
                writer.writerow([USER_ID, USERNAME,
                                str(task.get('completed')), task.get('title')])
