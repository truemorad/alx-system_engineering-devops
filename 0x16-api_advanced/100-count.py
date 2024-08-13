#!/usr/bin/python3
"""
Module for storing the count_words function.
"""
import requests


def count_words(subreddit, word_list, word_count=[], page_after=None):
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    if page_after:
        url += '?after={}'.format(page_after)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return
    try:
        data = response.json().get('data')
        page_after = data.get('after')
        children = data.get('children')
        for child in children:
            title = child.get('data').get('title').lower().split()
            for word in word_list:
                word_count.append(title.count(word.lower()))
        count_words(subreddit, word_list, word_count, page_after)
    except Exception:
        pass
    if not page_after:
        word_count = {word: word_count.count(word) for word in word_list}
        for key, value in sorted(word_count.items(), key=lambda x: x[1],
                                 reverse=True):
            if value > 0:
                print('{}: {}'.format(key, value))