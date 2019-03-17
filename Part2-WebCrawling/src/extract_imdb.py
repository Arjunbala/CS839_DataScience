from bs4 import BeautifulSoup
import csv
import requests

def extract_movie_names(soup):
    movie_list = []
    movies = soup.find_all('h3', {'class': 'lister-item-header'})
    for x in movies:
        for y in x.find_all('a'):
            movie_list.append(y.text)
    return movie_list

def extract_movie_years(soup):
    year_list = []
    movies = soup.find_all('span', {'class': 'lister-item-year'})
    for x in movies:
        year_list.append(x.text.split('(')[1].split(')')[0])
    return year_list

def extract_runtime(soup):
    runtime_list = []
    movies = soup.find_all('span', {'class': 'runtime'})
    for x in movies:
        runtime_list.append(x.text)
    return runtime_list

def extract_user_rating(soup):
    rating_list = []
    movies = soup.find_all('div', {'class': 'ipl-rating-star small'})
    for rating in movies:
        rating_list.append(rating.find('span',{'class':'ipl-rating-star__rating'}).text)
    return rating_list

def extract_metascores(soup):
    metascore_list = []
    movies = soup.find_all('span',{'class':'metascore'})
    for movie in movies:
        metascore_list.append(movie.text.strip())
    return metascore_list

def extract_directors(soup):
    directors_list = []
    movies = soup.find_all('p',{'class':'text-muted text-small'})
    for movie in movies:
        names = movie.find_all('a')
        if len(names) > 0:
            directors_list.append(names[0].text) 
    return directors_list

def extract_actors(soup):
    actors_list = []
    movies = soup.find_all('p',{'class':'text-muted text-small'})
    for movie in movies:
        names = movie.find_all('a')
        if len(names) > 0:
            all_names = ""
            for i in range(1, len(names)):
                all_names = all_names + names[i].text + ", "
            actors_list.append(all_names[0:len(all_names)-1])
    return actors_list

def extract_genres(soup):
    genre_list = []
    movies = soup.find_all('span',{'class':'genre'})
    for movie in movies:
        genre_list.append(movie.text.strip())
    return genre_list


base_url = 'https://www.imdb.com/list/ls063676189/?sort=list_order,asc&st_dt=&mode=detail&page='
movie_dict_list = []
id_no = 1
csv_columns = ['ID', 'Name', 'Year', 'Runtime', 'User Rating', 'Director', 'Actors', 'Genre']
for page_no in range(1,31):
    page_url = 'https://www.imdb.com/list/ls063676189/?sort=list_order,asc&st_dt=&mode=detail&page=' + str(page_no)
    print("Extracting from " + page_url)
    resp = requests.get(page_url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    names = extract_movie_names(soup)
    years = extract_movie_years(soup)
    runtimes = extract_runtime(soup)
    user_ratings = extract_user_rating(soup)
    #metascores = extract_metascores(soup)
    directors = extract_directors(soup)
    actors = extract_actors(soup)
    genres = extract_genres(soup)

    for i in range(0, len(names)):
        movie_dict = {}
        movie_dict['ID'] = ('%04d' % id_no)
        id_no = id_no + 1
        movie_dict['Name'] = names[i]
        movie_dict['Year'] = years[i]
        movie_dict['Runtime'] = runtimes[i]
        movie_dict['User Rating'] = user_ratings[i]
        #movie_dict['Metascore'] = metascores[i]
        movie_dict['Director'] = directors[i]
        movie_dict['Actors'] = actors[i]
        movie_dict['Genre'] = genres[i]
        movie_dict_list.append(movie_dict)

print(movie_dict_list)
try:
    with open('../data/imdb.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in movie_dict_list:
            writer.writerow(data)
except IOError:
    print("I/O error")
