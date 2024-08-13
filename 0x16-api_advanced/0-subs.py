#!/usr/bin/python3
def number_of_subscribers(subreddit):
    import requests
    api =     url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    if response.status_code == 404:
        return 0
    else: 
        return response.json().get('data').format('subscribers')