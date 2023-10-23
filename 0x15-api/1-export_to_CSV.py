#!/usr/bin/python3
"""display Employee Tasks info"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get("{}users/{}".format(url, argv[1])).json()
    todos = requests.get("{}users/{}/todos".format(url, argv[1])).json()

    tasks = []

    for todo in todos:
        tasks.append([todo.get("completed"), todo.get("title")])

    with open("{}.csv".format(user.get("id")), "w") as file:
        csv_writer = csv.writer(file, delimiter=",", quoting=csv.QUOTE_ALL)
        for task in tasks:
            csv_writer.writerow([user.get("id"), user.get("username")] + task)
