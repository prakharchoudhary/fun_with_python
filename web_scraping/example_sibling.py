from urllib.request import urlopen
from bs4 import BeautifulSoup

url = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(url, 'html.parser')


for sibling in bsObj.find("table", {"id": "giftList"}).tr.next_siblings:
	print(sibling)
