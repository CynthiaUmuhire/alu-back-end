#!/usr/bin/python3
"""
    python script that returns TODO list progress for a given employee ID
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    """
        request user info by employee ID
    """
    request_employee = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/'.format(argv[1]))
    """
        convert json to dictionary
    """
    employee = json.loads(request_employee.text)
    """
        extract employee name
    """
    e_name = employee.get("name")

    """
        request user's TODO list
    """
    request_todos = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1]))
    """
        dictionary to store task status in boolean format
    """
    tasks = {}
    """
        convert json to list of dictionaries
    """
    todos = json.loads(request_todos.text)
    """
        loop through dictionary & get completed tasks
    """
    for dictionary in todos:
        tasks.update({dictionary.get("title"): dictionary.get("completed")})

    """
        return name, total number of tasks & completed tasks
    """
    EMPLOYEE_NAME = e_name
    NUMBER_OF_TASKS = len(tasks)
    DONE_TASKS = len([k for k, v in tasks.items() if v is True])
    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, DONE_TASKS, NUMBER_OF_TASKS))
    for k, v in tasks.items():
        if v is True:
         k = todos.get("title")
            print("\t\b {}".format(k))
