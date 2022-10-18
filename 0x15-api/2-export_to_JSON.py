#!/usr/bin/python3
'''
This program write user data
to json file
'''

import requests
import sys

if __name__ == '__main__':
    emp_id = int(sys.argv[1])
    users_url = "https://jsonplaceholder.typicode.com/users/{}"
    emp_data = requests.get(users_url.format(emp_id)).json()
    emp_uname = emp_data.get('username')
    tasks = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    filename = str(emp_id) + '.json'
    tasks_obj = []
    with open(filename, mode='w') as f:
        for task in tasks:
            if task.get('userId') == emp_id:
                task_obj = {"task": task.get('title'),
                            "completed": task.get('completed'),
                            "username": emp_uname}
                tasks_obj.append(task_obj)
        json_obj = {str(emp_id): tasks_obj}
        f.write("{}".format(json_obj))
