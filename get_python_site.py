import requests


def get_request(url):
    response = requests.get(url)
    print(response)

get_request('https://www.python.org/')