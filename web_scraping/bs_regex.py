import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(url, 'html.parser')

images = bsObj.findAll("img", {"src": re.compile("\.\.\/img\/gifts\/img.*\.jpg")})

for image in images:
	print(image["src"])