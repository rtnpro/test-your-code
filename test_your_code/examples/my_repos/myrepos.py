import sys
import requests
import json

URL = "https://api.github.com/users/{user}/repos"

def sort_response_json(text, n):
    repos_list = json.loads(text)
    return [i['html_url'] for i in sorted(
        repos_list, key=lambda i: -1 * i['watchers'])][:n]


def most_watched_repos(user, n):
    url = URL.format(user=user)
    resp = requests.get(url, timeout=0.1)
    return sort_response_json(resp.content, n)


if __name__ == '__main__':
    user = sys.argv[1]
    n = int(sys.argv[2])
    print most_watched_repos(user, n)
