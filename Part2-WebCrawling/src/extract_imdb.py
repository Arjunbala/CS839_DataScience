from bs4 import BeautifulSoup
import requests

# TODO: Update URL
url = 'https://www.imdb.com/search/title?genres=action&start=0&explore=title_type,genres&ref_=adv_nxt'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')
movie_list = soup.find_all('h3',{'class':'lister-item-header'})
for x in movie_list:
    for y in x.find_all('a'):
        print(y.text)

