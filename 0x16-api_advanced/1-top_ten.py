#!/usr/bin/python3
'''Module for task 1'''


def top_ten(subreddit):
    '''method that print the top
    hot ranks'''
    import requests

    results = requests.get('https://www.reddit.com/r/{}/hot.json?limit=10'
                            .format(subreddit),
                            headers={'User-Agent': 'My-User-Agent'},
                            allow_redirects=False)
    if results.status_code >= 300:
        print('None')
    else:
        [print(result.get('data').get('title'))
         for result in results.json().get('data').get('children')]
