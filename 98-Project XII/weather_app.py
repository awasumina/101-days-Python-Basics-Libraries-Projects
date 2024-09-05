# pip install bs4

import requests
from bs4 import BeautifulSoup as soup

# search  = "Weather in Bhaktapur, Nepal"
search = input("Please provide the city name where you want to know the weather as 'Weather In Tokyo:\n'")
url = f"https://www.google.com/search?&q={search}" # this indicates the search paramter in the given url

response=requests.get(url)   # get method to fetch data from a website and store it into response object

s = soup(response.text,"html.parser") # This html parses/fetches the data from url

update = s.find("div", class_ = "BNeawe").text # built in class
print (update)  