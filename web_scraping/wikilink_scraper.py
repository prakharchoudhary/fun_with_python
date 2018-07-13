import re
import random
import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup

random.seed(datetime.datetime.now())
def getLinks(articleURL):
	url = urlopen("https://en.wikipedia.org"+articleURL)
	soup = BeautifulSoup(url, 'html.parser')

	return soup.find("div", {"id":"bodyContent"}).findAll("a",
							href= re.compile("^(/wiki/)((?!:).)*$"))
							#href should have /wiki/, should not contain ':'
							# and can carry any character.
	

string = input("Enter the term to be searched: ")
string = string.split(" ")
search = '_'.join(string)
print(search)
links = getLinks('/wiki/{}'.format(search))
while len(links)>0:
	newArticle = links[random.randint(0, len(links)-1)].attrs['href']
	print(newArticle)
	links = getLinks(newArticle)


