#!/usr/bin/python3
"""
 a script that returns top ten hot title for a post.
"""
import requests


def recurse(subreddit, hot_list=[]):
    api = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(api, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        print(None)
    else:
        for post in response.json().get('data').get('children'):
            hot_list.append(post.get('data').get('title'))
