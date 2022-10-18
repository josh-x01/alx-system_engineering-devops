#!/usr/bin/python3
'''
This program write user data
to csv file
'''

import requests
import sys

if __name__ == '__main__':
    emp_id = int(sys.argv[1])
    users_url = "https://jsonplaceholder.typicode.com/users/{}"
    emp_data = requests.get(users_url.format(emp_id)).json()
    emp_uname = emp_data.get('username')
    tasks = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    filename = str(emp_id) + '.csv'
    with open(filename, mode='w') as f:
        for task in tasks:
            if task.get('userId') == emp_id:
                f.write('"{:d}","{:s}","{}","{:s}"\n'.format(emp_id,
                        emp_uname, task.get('completed'), task.get('title')))
