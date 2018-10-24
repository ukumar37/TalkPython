import requests
import collections

MovieResult = collections.namedtuple(
    'MovieResult',
    'imdb_code, title, duration, director, year, rating, imdb_score, keywords, genre'
)

search = input("What movie do you want to search for?")  # key word in movie title
url = 'http://movie_service.talkpython.fm/api/search/{}'.format(search)

resp = requests.get(url)  # execute the api and get the movie data
resp.raise_for_status()  # check for status code

movie_data = resp.json()  # get the movie data in json format, this will return a dictionary object
movies_list = movie_data.get('hits')  # get the hit movies only, this will return a list object

movies = []  # start with an empty list of movies
for md in movies_list:  # loop movies_list and populate the MovieResult tuple defined earlier
    m = MovieResult(
        imdb_code=md.get('imdb_code'),
        title=md.get('title'),
        duration=md.get('duration'),
        director=md.get('director'),
        year=md.get('year', 0),
        rating=md.get('rating', 0),
        imdb_score=md.get('imdb_score', 0.0),
        keywords=md.get('keywords'),
        genre=md.get('genre')
    )
    movies.append(m)

print("Found {} movies for search '{}'. Here is the list:".format(len(movies), search))
for m in movies:
    print("{} -- {}".format(m.year, m.title))


#  print(type(movies_list), movies_list)
