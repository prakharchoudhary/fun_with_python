#for wikipedia

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(articleURL):
	global pages
	url = urlopen("https://en.wikipedia.org"+articleURL)    #change url to change the target site to be crawled
	soup = BeautifulSoup(url, 'html.parser')

	for link in soup.findAll("a", href=re.compile("^(/wiki/)")):
		if 'href' in link.attrs:
			if link.attrs['href'] not in pages:
				#We encountered a new page
				newPage = link.attrs['href']
				print(newPage)
				pages.add(newPage)
				getLinks(newPage)

getLinks("")