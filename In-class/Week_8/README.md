# Web Scraping Script

## What did you want to answer here?
There is always a notion in popular culture that the most critically acclaimed and often "best" movies were released during the 1970s. Based on the user generated [IMDB list of the Top 250 movies](https://www.imdb.com/chart/top/?ref_=nv_mv_250), what is the proportion of movies released in the 1970s? Does the data back this up?
If not, what decade has the most entries in the list? And what proportion do they make up?

## What does this do?
This python script calls IMDB's Top 250 movies webpage and scrapes the release years for each movie on the list. The data is then cleaned, sorted, and manipulated in order to be able to present a user with some basic data such as, the proportion of movies from the 1970's versus those from the aughts and twenty-tens.

## How does it work?
* Using the urllib library, the script pulls the HTML from the website and stores it in a variable
* Then we apply BeautifulSoup's html parser to extract specific elements of HTML relevant for our question.
    - I use the find_all method to identify the `<td>` tage to pull the `TitleColumn` data.
    - From that point I use the find method to pull string data in the `<span>` tag which is the release year..
* Then I use some list comprehensions to clean the data and sort each release year into unique lists corresponding to their decades.
* From there I do some caluclations on the number of elements in each decade list to determine the proportions
* Finally the last thing I do is print some basic stats to the user about what I've discovered along with some data to back that up.
    - The final piece of information is each decade's proportion of the Top 250 list.

## Pretty cool, but is that all?
No! I'd like to build this out so that the data is dumped in some hard-coded slightly ham-fisted way. I'm working on used pandas to produce some data visualization to make this a little easier to parse. Additionally substituting some of the lists and using json objects or csvs might make this a little more object-oriented.