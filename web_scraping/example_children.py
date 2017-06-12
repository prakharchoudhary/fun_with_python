from urllib.request import urlopen
from bs4 import BeautifulSoup

url = urlopen("http://www.pythonscraping.com/pages/page3.html")

bsObj = BeautifulSoup(url, "lxml")

for child in bsObj.find("table", {"id": "giftList"}).children:
	print(child)
