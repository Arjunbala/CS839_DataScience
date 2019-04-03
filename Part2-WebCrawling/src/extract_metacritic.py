from bs4 import BeautifulSoup
import requests

def main():
	base_url = 'https://www.metacritic.com/browse/movies/score/metascore/all/filtered'


	resp = requests.get(base_url, headers={'User-Agent': 'Mozilla/5.0'})
	soup = BeautifulSoup(resp.text, 'html.parser')

	years = []
	movie_links = soup.find_all('a',{"class" : "title"})
	movie_names = []
	user_scores = []
	meta_scores = []
	directors = [] 
	actors = []
	genres = []
	for movie in movie_links :
		link = 'https://www.metacritic.com' + movie['href']
		resp_t = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
		soup_t = BeautifulSoup(resp_t.text, 'html.parser')
		movie_name = soup_t.find('h1').string
		print(movie_name)
		movie_names.append(movie_name)
		user_rating = soup_t.find('span', {'class' :"metascore_w user med_small movie positive"}).string
		print(user_rating)
		user_scores.append(user_rating)
		meta_rating = soup_t.find('div', {'class' : "metascore_w header_size movie positive indiv perfect" } ).string
		print(meta_rating)
		meta_scores.append(meta_rating)
		release_year = 	(soup_t.find('div', {'class' : 'details_section'}).find_all('span')[2]).find_all('span')[1].string.split(',')[1].lstrip()
		print(release_year)
		years.append(release_year)
		director = soup_t.find('div',{'class':"director"}).find('a').find('span').string
		print(director)
		directors.append(director)
		cast = soup_t.find('div',{'class' : "summary_cast details_section"}).find_all('a')
		stars = []
		for star in cast :
			stars.append(star.string)
		print(stars)
		actors.append(stars)
		genres_list = soup_t.find('div', {'class' : "genres"}).find_all('span')[1].find_all('span')
		for gen in genres_list :
			genres.append(gen.string)
		print(genres)

		break


	# print(len(movie_names))
	# print(movie_names)

	# movie_list = soup.find_all('h3')
	# 

	# for a in movie_list :
	# 	print(a.string)


if __name__ == "__main__":
    main()
