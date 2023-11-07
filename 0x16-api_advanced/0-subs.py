#!/usr/bin/python3
""" returns the number of subscribers """
import sys
import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-agent': 'Mozilla/5.0'}
    req = requests.get(url, headers=headers, allow_redirects=False)

    if req.status_code == 404:
        return 0
    return req.json().get("data").get("subscribers")
