#!/usr/bin/python3
"""display Employee Tasks info"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get("{}users/{}".format(url, argv[1])).json()
    todos = requests.get("{}users/{}/todos".format(url, argv[1])).json()

    user_id = str(user.get("id"))

    json_data = {user_id: []}

    for todo in todos:
        tmp_dict = {}
        tmp_dict["task"] = todo.get("title")
        tmp_dict["completed"] = todo.get("completed")
        tmp_dict["username"] = user.get("username")
        json_data.get(user_id).append(tmp_dict)

    with open("{}.json".format(user_id), "w") as file:
        json.dump(json_data, file)
