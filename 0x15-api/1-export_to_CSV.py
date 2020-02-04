#!/usr/bin/python3
"""Extend your Python script to export data in the CSV format."""

import csv
import requests
from sys import argv

if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"
    USER_ID = argv[1]
    user_req = requests.get("{}users/{}".format(url, USER_ID)).json()
    USERNAME = user_req["username"]
    todo_req = requests.get("{}todos?userId={}".format(url, USER_ID)).json()
    filename = "{}.csv".format(USER_ID)
    with open(filename, "w") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for user in todo_req:
            writer.writerow([argv[1], USERNAME, user.get("completed"),
                             user.get("title")])
