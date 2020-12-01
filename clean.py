from time import sleep
import requests

headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": "token xxxxxxxxxx",  # github授权token
    "X-OAuth-Scopes": "repo"
}

with open('./repos.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()

url = "https://api.github.com/repos/{}/{}"
urls = []
for line in data:
    print(line)
    name, repo = line.strip().split("/")
    urls.append(url.format(name, repo))

for url in urls:
    print(url)
    requests.delete(url=url, headers=headers)
    print('deleted->'+url)
