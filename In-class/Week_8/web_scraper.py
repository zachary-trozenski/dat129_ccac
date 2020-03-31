"""
Scraping demo, following along in class.
Before scraping check:
    1 - Are the URLs encoded sensibly
    such that we can use the urlib to grab
    the HTML page easily?
    2 - Are the elements on the page we want to
    scrape enclosed in HTML tags with distinct 
    names or tag names?

My experiment:
https://www.imdb.com/chart/top/?ref_=nv_mv_250

What proportion of the Top Rated movies are from
the 1970s?
"""

import urllib.request
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

def get_html_text(url):
    """
    Function takes a URL and grabs the HTML from the internet
    """
    # build request object
    request = urllib.request.Request(url)
    # access network via standard gateway
    # to retrieve HTML from the IMDB server
    with urllib.request.urlopen(request) as reply:
        return reply.read()

imdb_html = get_html_text(url)

#print just to check it works
#print(imdb_html)

# Pass raw HTML and desired parser to beautiful soup
soup = BeautifulSoup(imdb_html, 'html.parser')

movie_years = []

# with html passed to BeautifulSoup we can extract components
# 2ith spcific calls to find or find all
movie_titles = soup.find_all('td', 'titleColumn')

# for movies in movie_titles:
#     year = movies.find('span', 'secondaryInfo')
#     movie_years.append(movies)

for movies in movie_titles:
    year = movies.find('span').string
    movie_years.append(year)
    #print(year)

print(movie_years)

#print(movie_titles)

#total_films = 250
#seventies_films = []

# movie titles is an iterable and contains all the mini-trees
# who's parent is an <a> tag of class title
# for movies in movie_titles:
#     year = movies.find('span').string
#     print(year)

# 
# if movie_year in range(1970,1981):
    # seventies_films.append(movie_year)
# proportion = len(seventies_films) / total_films
# print statment with the proportion

# i'd also like to print the titles that were released in the 70s












