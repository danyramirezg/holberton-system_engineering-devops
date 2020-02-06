#!/usr/bin/python3

"""Function that queries the Reddit API and prints the titles of the first 10
 hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """If not a valid subreddit, print None.
NOTE: Invalid subreddits may return a redirect to search results."""

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    header = \
        {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0)"}

    resp = requests.get(url, headers=header)

    if resp.status_code == 200:
        data = resp.json().get("data").get("children")

        for children in data:
            tittle = children.get("data").get("title")
            print(tittle)

    else:
        print('None')
