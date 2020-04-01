"""
Before scraping check:
    1 - Are the URLs encoded sensibly
    such that we can use the urlib to grab
    the HTML page easily?
    2 - Are the elements on the page we want to
    scrape enclosed in HTML tags with distinct 
    names or tag names?

Site i'm using to scrape:
https://www.imdb.com/chart/top/?ref_=nv_mv_250

Research question:
The 1970's is often lauded as producing some of the most critically
acclaimed films in cinematic history. However, how many of IMDB's Top
250 films are actually from the 70's and what is the proportion of the whole?
If not the seventies, then which decade is the most "critically acclaimed"?

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

# Pass raw HTML and desired parser to beautiful soup
soup = BeautifulSoup(imdb_html, 'html.parser')

## Initialize some lists to store figures pulled from the html data
# This list will house raw extracted movie years
movie_years = []
# This list will house the cleaned years sliced from movie_years
clean_years = []

# These lists will house each year counted in the list of 250 for the decade
# in which they were released
twenties_films = []
thirties_films = []
forties_films = []
fifties_films = []
sixties_films = []
seventies_films = []
eighties_films = []
nineties_films = []
aughts_films = []
teens_films = []

# initialize a list of all sorted release years to iterate over later
all_films = [
twenties_films,
thirties_films,
forties_films,
fifties_films,
sixties_films,
seventies_films,
eighties_films,
nineties_films,
aughts_films,
teens_films]

# locate all instances of the <td> tag in the html
# and pull the title column fields from within that tag
movie_titles = soup.find_all('td', 'titleColumn')

# iterate of the html lines extracted by pulling out the release years
# in string format and add it to the movie_years list
for movies in movie_titles:
    year = movies.find('span').string
    movie_years.append(year)

# iterate over each of the raw release years in the movie_years list
# and slice the list elements so only the digits are extracted
for films in movie_years:
    clean_years.append(films[1:5])

# iterate over the list of cleaned release years in clean_years and
# sort them into lists representing each decade from 1920 to 2019
for flicks in clean_years:
    if int(flicks) in range(1970,1980):
        seventies_films.append(flicks)
    if int(flicks) in range(1920,1930):
        twenties_films.append(flicks)
    if int(flicks) in range(1930,1940):
        thirties_films.append(flicks)
    if int(flicks) in range(1940,1950):
        forties_films.append(flicks)
    if int(flicks) in range(1950,1960):
        fifties_films.append(flicks)
    if int(flicks) in range(1960,1970):
        sixties_films.append(flicks)
    if int(flicks) in range(1980,1990):
        eighties_films.append(flicks)
    if int(flicks) in range(1990,2000):
        nineties_films.append(flicks)
    if int(flicks) in range(2000,2010):
        aughts_films.append(flicks)
    if int(flicks) in range(2010,2020):
        teens_films.append(flicks)

# intialize some variables to be used for calculations
total_films = 250
proportions = []

# calculate the proportions for each decade and store them in a list
for entries in all_films:
    proportions.append((len(entries)/total_films) * 100)

print()
print("Out of the Top 250 films from IMDB,", len(seventies_films), "are from the 1970's.")
print("Percentage of Top 250 films from the 1970's: {:2.2}%".format(proportions[int(5)]))
print()
print("The two decades with the most entires in IMDB's Top 250 are the early 2000's" +
    " and the 2010's with", len(aughts_films), "films a piece.")
print("The proportions of films from each decade (in ascending order) are: ")

for percents in proportions:
    print("{:.2f}%".format(percents))


###
# SCRATCH
###

# check to make sure all 250 are accounted for
# for entries in all_films:
#     print(len(entries))

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

# for movies in movie_titles:
#     year = movies.find('span', 'secondaryInfo')
#     movie_years.append(movies)

# i'd also like to print the titles that were released in the 70s