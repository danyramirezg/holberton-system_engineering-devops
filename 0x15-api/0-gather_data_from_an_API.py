#!/usr/bin/python3
"""Python script that, using a REST API, for a given employee ID, returns
 information about his/her TODO list progress."""

import requests
from sys import argv

if __name__ == "__main__":

    """
    """

    url = "https://jsonplaceholder.typicode.com/"
    var = requests.get("{}users/{}".format(url, argv[1])).json()
    employee_name = var["name"]
    number_total_tasks = len(requests.get("{}todos?userId={}"
                                          .format(url, argv[1])).json())
    number_done_tasks = len(requests.get("{}todos?userId={}&&completed=true"
                                         .format(url, argv[1])).json())
    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, number_done_tasks, number_total_tasks))
    topic = requests.get("{}todos?userId={}&&completed=true"
                         .format(url, argv[1])).json()
    for i in topic:
        print("\t " + i["title"])
