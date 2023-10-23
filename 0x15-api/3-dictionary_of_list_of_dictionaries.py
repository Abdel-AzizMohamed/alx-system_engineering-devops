#!/usr/bin/python3
"""display Employee Tasks info"""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    users = requests.get("{}users".format(url)).json()
    json_data = {}

    for user in users:
        user_id = str(user.get("id"))
        todos = requests.get("{}users/{}/todos".format(url, user_id)).json()

        json_data[user_id] = []

        for todo in todos:
            tmp_dict = {}
            tmp_dict["username"] = user.get("username")
            tmp_dict["task"] = todo.get("title")
            tmp_dict["completed"] = todo.get("completed")
            json_data.get(user_id).append(tmp_dict)

    with open("todo_all_employees.json", "w") as file:
        json.dump(json_data, file)
