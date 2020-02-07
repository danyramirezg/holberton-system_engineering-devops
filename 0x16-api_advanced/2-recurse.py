#!/usr/bin/python3

"""Function that queries the Reddit API and prints the titles of the first 10
 hot posts listed for a given subreddit"""

import requests

titles = []


def recurse(subreddit, hot_list=[], after=None):
    if after:
        url = \
            "https://www.reddit.com/r/" \
            "{}/hot.json?limit=100&after={}".format(subreddit, after)
    else:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    header = \
        {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0)"}

    resp = requests.get(url, headers=header)
    # "https://www.reddit.com/r/{}/hot.json"

    if resp.status_code != 200:
        return None

    if resp.status_code == 200:
        data = resp.json().get("data").get("children")
        after = resp.json().get("data").get("after")

        if data is None:
            return None

        for children in data:
            tittle = children.get("data").get("title")
            # print(tittle)
            hot_list.append(tittle)

    # print(after)

    if after:
        recurse("{}".format(subreddit), after=after)
    return hot_list
