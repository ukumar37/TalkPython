import requests
import collections

MovieResult = collections.namedtuple(
    'MovieResult',
    'imdb_code, title, duration, director, year, rating, imdb_score, keywords, genres'
)


def find_movies(search_text):
    url = 'http://movie_service.talkpython.fm/api/search/{}'.format(search_text)

    resp = requests.get(url)  # execute the api and get the movie data
    resp.raise_for_status()  # check for status code

    movie_data = resp.json()  # get the movie data in json format, this will return a dictionary object
    movies_list = movie_data.get('hits')  # get the hit movies only, this will return a list object

    movies = [
        MovieResult(**md)
        for md in movies_list
    ]

    return(movies)