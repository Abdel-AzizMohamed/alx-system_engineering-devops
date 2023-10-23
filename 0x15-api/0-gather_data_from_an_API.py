#!/usr/bin/python3
# display Employee Tasks info
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get("{}users/{}".format(url, argv[1])).json()
    todos = requests.get("{}users/{}/todos".format(url, argv[1])).json()

    complete = []

    for todo in todos:
        if todo["completed"]:
            complete.append(todo["title"])

    print("Employee {} is done with tasks({}/{}):".format(user["name"],
          len(complete), len(todos)))
    for item in complete:
        print("\t{}".format(item))
