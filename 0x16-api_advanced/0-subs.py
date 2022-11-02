#!/usr/bin/python3
"""Module for task 0"""
import requests


def number_of_subscribers(subreddit):
    """" A method that return the number of
    reddit subscribers """

    result = requests.get("https://www.reddit.com/r/{}/about.json"
                          .format(subreddit),
                          headers={"User-Agent": "My-User-Agent"},
                          allow_redirects=False)
    if result.status_code >= 300:
        return 0
    return result.json().get("date").get("subscribers")
