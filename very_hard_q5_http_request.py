"""
HTTP Requests
The requests module is an HTTP library. You will be using it here to retrieve movie titles from the imdb.com website.
See Resources for more details, but all you need for this challenge is get() and .text.
The movie title can be easily located in the text of the web page because it is preceded by the HTML tag:
 <title> and followed by the tag: </title>.

The requests module is not a standard module but it can be accessed from the Edabit code editor.
Improvise a function that takes an imdb.com address and returns the title of the movie at that address.

Examples
movie_title('https://www.imdb.com/title/tt0111161/') = 'The Shawshank Redemption (1994) - IMDb'
movie_title('https://www.imdb.com/title/tt0108052/') = 'Schindler's List (1993) - IMDb'
movie_title('https://www.imdb.com/title/tt0073486/') = 'One Flew Over the Cuckoo's Nest (1975) - IMDb'
"""
import requests


def movie_title(url):
    movie = requests.get(url)
    start = movie.text.find('<title>') + len('<title>')
    end = movie.text.find('</title>')
    return movie.text[start:end]
