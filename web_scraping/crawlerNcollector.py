from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(articleURL):
	global pages
	url = urlopen("https://en.wikipedia.org"+articleURL)    #change url to change the target site to be crawled
	soup = BeautifulSoup(url, 'lxml')
	try:
		print(soup.h1.get_text())
		print(soup.find(id="mw-content-text").findAll("p")[0])
		print(soup.find(id="ca-edit").find("span").find("a").attrs['href'])
	except AttributeError:
		print("This page is missing something! No worries though.")

	except UnicodeEncodeError:
		pass

	for link in soup.findAll("a", href=re.compile("^(/wiki/)")):
		if 'href' in link.attrs:
			if link['href'] not in pages: 
				newPage = link.attrs['href']
				print('-----------------------------------------------\n'+newPage)
				pages.add(newPage)
				getLinks(newPage)
getLinks("")