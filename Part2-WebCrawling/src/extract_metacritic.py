from bs4 import BeautifulSoup
import requests

# TODO: Update URL
url = 'https://www.metacritic.com/browse/movies/score/metascore/all/filtered?page=0'
session = requests.Session()

resp = session.get(url, headers={'User-Agent': 'Mozilla/5.0'})

soup = BeautifulSoup(resp.text, 'html.parser')
movie_list = soup.find_all('a', {'class': 'title'})
for x in movie_list:
    for y in x.find_all('h3'):
        print(y.text)
