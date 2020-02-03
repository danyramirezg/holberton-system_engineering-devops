#!/usr/bin/python3
"""Python script that, using a REST API, for a given employee ID, returns
 information about his/her TODO list progress."""

import requests
from sys import argv

if __name__ == "__main__":
    var = requests.get(
        "https://jsonplaceholder.typicode.com/users/" + argv[1]).json()
    employee_name = var["name"]
    number_total_tasks = len(requests.get("https://jsonplaceholder.typicode"
                                          ".com/todos?userId={}".
                                          format(argv[1])).json())
    number_done_tasks = len(requests.get("https://jsonplaceholder.typicode"
                                         ".com/todos?userId={}&&completed=true"
                                         .format(argv[1])).json())

    topic = requests.get("https://jsonplaceholder.typicode.com/todos?userId"
                         "={}&&completed=true".format(argv[1])).json()
    result = "Employee {} is done with tasks({}/{}):".format(
        employee_name,
        number_done_tasks,
        number_total_tasks)
    print(result)
    for i in topic:
        print("\t" + i["title"])
