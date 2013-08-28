import sys
import requests
import json

URL = "https://api.github.com/users/{user}/repos"

def most_watched_repos(user, n):
    url = URL.format(user=user)
    resp = requests.get(url, timeout=10)
    repos_list = json.loads(resp.content)
    return [i['html_url'] for i in sorted(
        repos_list, key=lambda i: -1 * i['watchers'])][:n]


if __name__ == '__main__':
    user = sys.argv[1]
    n = int(sys.argv[2])
    print most_watched_repos(user, n)
