#!/usr/bin/python3
'''module for top ten post'''
import requests


def top_ten(subreddit):
    '''prints the top ten hot post'''

    results = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                           .format(subreddit),
                           headers={"User-Agent": "My-User-Agent"},
                           allow_redirects=False)
    if results.status_code >= 300:
        print('None')
    else:
        [print(result.get('data').title)
            for result in results.json().get('data').get('children')]
