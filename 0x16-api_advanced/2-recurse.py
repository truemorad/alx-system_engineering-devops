#!/usr/bin/python3
"""
i miss c :(
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    api = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after}
    response = requests.get(api, headers=headers,
                            allow_redirects=False, params=params)
    if response.status_code == 200:
        for post in response.json().get('data').get('children'):
            hot_list.append(post.get('data').get('title'))
        after = response.json().get("data").get("after")
    else:
        return None
    if after is None:
        return hot_list
    else:
        return recurse(subreddit, hot_list, after)
