from bs4 import BeautifulSoup
import requests
import pandas as pd
import time

def main():
	years = []
	movie_names = []
	user_scores = []
	meta_scores = []
	directors = [] 
	actors = []
	genres_list = []
	runtimes = []
	ids = []
	id_init = 2800
	#Code to extract information about 3000 movies from metacritic
	for i in range(28,32) :
		if i == 0:
			base_url = 'https://www.metacritic.com/browse/movies/score/metascore/all/filtered' 
		else :
			base_url = 'https://www.metacritic.com/browse/movies/score/metascore/all/filtered?page=' + str(i)
		print(base_url)
		resp = requests.get(base_url, headers={'User-Agent': 'Mozilla/5.0'})
		soup = BeautifulSoup(resp.text, 'html.parser')
		flag = False
		movie_links = soup.find_all('a',{"class" : "title"})
		for movie in movie_links :
			link = 'https://www.metacritic.com' + movie['href']
			resp_t = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
			soup_t = BeautifulSoup(resp_t.text, 'html.parser')

			try :
				movie_name = soup_t.find('h1').string
				# print(movie_name)
			except :
				movie_name = ''
				# continue

			try :
				user_rating = soup_t.find('span', {'class' :"metascore_w user med_small movie positive"}).string
				# print(user_rating)
			except :
				user_rating = ''
				# continue
			
			try :
				meta_rating = soup_t.find('div', {'class' : "metascore_w header_size movie positive indiv perfect" } ).string
				# print(meta_rating)
			except :
				meta_rating = ''
				# continue
			
			try:
				release_year = 	(soup_t.find('div', {'class' : 'details_section'}).find_all('span')[-1]).string.split(',')[1].lstrip()
				# print(soup_t.find('div', {'class' : 'details_section'}).find_all('span'))
				# print(release_year)
			except :
				release_year = ''
				# continue
			
			try:
				director = soup_t.find('div',{'class':"director"}).find('a').find('span').string
				# print(director)
			except :
				director = ''
				# continue

			try:
				cast = soup_t.find('div',{'class' : "summary_cast details_section"}).find_all('a')
				stars = ''
				for star in cast :
					stars += star.string + ', '
				# print(stars)
				stars = stars[:-2]
			except :
				stars = ''
				# continue


			try:
				gen_list = soup_t.find('div', {'class' : "genres"}).find_all('span')[1].find_all('span')
				genres = ''
				for gen in gen_list :
					genres += gen.string + ', '
				genres = genres[:-2]
				# print(genres)
			except :
				genres = ''
				# continue
			
			try:
				rt = soup_t.find('div', { 'class' : "runtime"}).find_all('span')[1].string
				# print(rt)
			except :
				rt = ''
				# continue

			movie_names.append(movie_name)
			user_scores.append(user_rating)
			meta_scores.append(meta_rating)
			years.append(release_year)
			directors.append(director)
			actors.append(stars)
			genres_list.append(genres)
			runtimes.append(rt)
			id_init += 1
			ids.append(id_init)
			if len(movie_names) == 3000 :
				flag = True
			if flag :
				break
		if flag :
			break
		time.sleep(30)

	df = pd.DataFrame({
	    'ID': ids,
	    'Name': movie_names,
	    'Year': years,
	    'Runtime': runtimes,
	    'User Rating': user_scores,
	    'Metascore': meta_scores,
	    'Director': directors,
	    'Actors': actors,
	    'Genre': genres_list
	})
	# df.to_csv('../data/metacritic.csv', index=False)
	with open('../data/metacritic.csv', 'a') as f:
		df.to_csv(f, index=False, header=False)

			




if __name__ == "__main__":
    main()
