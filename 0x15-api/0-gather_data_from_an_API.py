#!/usr/bin/python3
'''
This program displays number of completed
tasks for a given userId
'''

import requests
import sys

if __name__ == '__main__':
    emp_id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com/users/{}"
    emp_data = requests.get(url.format(emp_id)).json()

    emp_name = emp_data.get('name')

    tasks = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    tasks_compl = 0
    tasks_compl_title = []
    for task in tasks:
        if task.get('userId') == emp_id:
            if task.get('completed'):
                tasks_compl += 1
                tasks_compl_title.append(task.get('title'))
    msg = "Employee {:s} is done with tasks({:d}/20):"
    print(msg.format(emp_name, tasks_compl))
    for title in tasks_compl_title:
        print('\t {:s}'.format(title))
