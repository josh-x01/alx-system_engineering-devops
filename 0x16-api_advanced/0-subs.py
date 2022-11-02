#!/usr/bin/python3
<<<<<<< HEAD
"""Module for task 0"""


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    to the subreddit"""
    import requests

    sub_info = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if sub_info.status_code >= 300:
        return 0

    return sub_info.json().get("data").get("subscribers")
=======
"""Module for reddit subs"""


def number_of_subscribers(subreddit):
    """"
        A method that return the number of
        reddit subscribers
    """
    import requests

    result = requests.get("https://www.reddit.com/r/{}/about.json"
                          .format(subreddit),
                          headers={"User-Agent": "My-User-Agent"},
                          allow_redirects=False)
    if result.status_code >= 300:
        return 0
    return result.json().get("date").get("subscribers")
>>>>>>> parent of c55dbed... reddit subs
