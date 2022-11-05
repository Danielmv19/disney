import requests
import random
pagerandom = random.randint(1, 41)
idrandom = random.randint(5, 15)
print(pagerandom)
print(idrandom)
url = "https://api.disneyapi.dev/characters?page={}".format(pagerandom)
r = requests.get(url)
j = r.json()
r = idrandom
name = j["data"][r]['name']
img = j["data"][r]['imageUrl']
films = j["data"][r]['films']
shortFilms = j["data"][r]['shortFilms']
tvShows = j["data"][r]['tvShows']
videoGames = j["data"][r]['videoGames']
parkAttractions = j["data"][r]['parkAttractions']
print(f'Nombre:  {name}\nFilms:  {films}\nShortFilms:  {shortFilms}\nTvShows:  {tvShows}\nVideoGames:  {videoGames}\nParkAttractions:  {parkAttractions}\n')

