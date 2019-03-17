from bs4 import BeautifulSoup
import requests

# TODO: Update URL
url = 'https://www.imdb.com/list/ls063315922/'
resp = requests.get(url)
soup = BeautifulSoup(resp.text)
movie_list = soup.find_all('h3',{'class':'lister-item-header'})
for x in movie_list:
    for y in x.find_all('a'):
        print(y.text)
