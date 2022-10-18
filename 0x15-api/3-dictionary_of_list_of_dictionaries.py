#!/usr/bin/python3
'''
This program write user data
to json file
'''

import json
import requests
import sys

if __name__ == '__main__':
    usr_url = "https://jsonplaceholder.typicode.com/users"
    emps_data = requests.get(usr_url).json()
    tasks = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    filename = "todo_all_employees.json"
    tasks_obj = []
    all_tasks = {}
    _min = 0
    _max = 20

    with open(filename, mode='w') as f:
        for emp_data in emps_data:
            for i in range(_min, _max):
                task = tasks[i]
                task_obj = {"task": task.get('title'),
                            "completed": task.get('completed'),
                            "username": emp_data.get('username')}
                tasks_obj.append(task_obj)

            all_tasks[str(emp_data.get('id'))] = tasks_obj
            tasks_obj = []
            _min = _max
            _max = _max + 20

        json.dump(all_tasks, f)
