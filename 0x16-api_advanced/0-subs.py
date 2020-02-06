#!/usr/bin/python3
"""function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers)
for a given subreddit. If an invalid subreddit is given, the function should return 0"""

import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0)"}
    resp = requests.get(url, headers=header)

    if resp.status_code == 200:
        data = resp.json().get("data")
        subs = data.get("subscribers")
        return subs
    else:
        return 0
