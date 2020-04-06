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

To do:
- Refactor code into dictionary (csv for pandas/matplotlib)
- using matplotlib
    - %matplotlib inline (for jupiter notebooks)

"""

from bs4 import BeautifulSoup
import json
import urllib.request
# import matplotlib

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

# initialize a data dictionary that will house all the data we'll want to 
# store and reference later (replaces all those pesky lists)
cleaning_dict = {
"movie_years" : [],
"clean_years" : [],
}

decade_dict = {
"twenties_films" : [],
"thirties_films" : [],
"forties_films" : [],
"fifties_films" :[],
"sixties_films" : [],
"seventies_films" : [],
"eighties_films" : [],
"nineties_films" : [],
"aughts_films" : [],
"teens_films" : []
}

proportions = []

# locate all instances of the <td> tag in the html
# and pull the title column fields from within that tag
movie_titles = soup.find_all('td', 'titleColumn')

# iterate of the html lines extracted by pulling out the release years
# in string format and add it to the movie_years list
for movies in movie_titles:
    year = movies.find('span').string
    cleaning_dict["movie_years"].append(year)

# iterate over each of the raw release years in the movie_years list
# and slice the list elements so only the digits are extracted
for films in cleaning_dict["movie_years"]:
    cleaning_dict["clean_years"].append(films[1:5])

# iterate over the list of cleaned release years in clean_years and
# sort them into lists representing each decade from 1920 to 2019
for flicks in cleaning_dict["clean_years"]:
    if int(flicks) in range(1920,1930):
        decade_dict["twenties_films"].append(flicks)
    if int(flicks) in range(1930,1940):
        decade_dict["thirties_films"].append(flicks)
    if int(flicks) in range(1940,1950):
        decade_dict["forties_films"].append(flicks)
    if int(flicks) in range(1950,1960):
        decade_dict["fifties_films"].append(flicks)
    if int(flicks) in range(1960,1970):
        decade_dict["sixties_films"].append(flicks)
    if int(flicks) in range(1970,1980):
        decade_dict["seventies_films"].append(flicks)
    if int(flicks) in range(1980,1990):
        decade_dict["eighties_films"].append(flicks)
    if int(flicks) in range(1990,2000):
        decade_dict["nineties_films"].append(flicks)
    if int(flicks) in range(2000,2010):
        decade_dict["aughts_films"].append(flicks)
    if int(flicks) in range(2010,2020):
        decade_dict["teens_films"].append(flicks)

# intialize some variables to be used for calculations
total_films = 250

# calculate the proportions for each decade and store them in a list
for entries in decade_dict:
    proportions.append((len(entries)/total_films) * 100)

# print()
# print("Out of the Top 250 films from IMDB,", len(seventies_films), "are from the 1970's.")
# print("Percentage of Top 250 films from the 1970's: {:2.2}%".format(proportions[int(5)]))
# print()
# print("The two decades with the most entires in IMDB's Top 250 are the early 2000's" +
#     " and the 2010's with", len(aughts_films), "films a piece.")
# print("The proportions of films from each decade (in ascending order) are: ")

# for percents in decade_dict["proportions"]:
#     print("{:.2f}%".format(percents))

print(decade_dict)
print(proportions)

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