import requests
import _collections

search = 'capital'
url = 'http://movie_service.talkpython.fm/api/search/{}'.format(search)

resp = requests.get(url)

print(resp.status_code)