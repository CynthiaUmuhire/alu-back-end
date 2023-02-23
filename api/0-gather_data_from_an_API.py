#!/usr/bin/python3
"""Module"""

import requests

import sys

if __name__ == "__main__":

    users = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/'.format(argv[1]))
        
        user = json.loads(users.text)

    name = user.get("name")

    request_todos =requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1]))
    todos = json.loads(request_todos.text)  
    t_Tasks = 0
    completed = 0
    i = 1
    

    for i in todos.json():
        if user.get('userId') == i:
            t_Tasks += 1
            if t in todos.items() is True:
                completed += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(name, completed, totalTasks))

     if todos.items()is True:
         print('\n'.join(["\t " + user.get('title') for task in todos.json()
