#scraping data from a specific tag ---> using findAll

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html)

nameList = bsObj.findAll("span", {"class": "green"})
for name in nameList:
	print(name.get_text())
