from urllib.request import urlopen
from bs4 import BeautifulSoup

pages = set()
text = []
def getLinks(url):
	global pages

	link = urlopen("https://cdn.hackerrank.com/hackerrank/static/contests/capture-the-flag/infinite/"+url)
	obj = BeautifulSoup(link, "html.parser")
	for l in obj.findAll("a"):
		if "href" in l.attrs:
			if l.attrs["href"] not in pages:
				try:
					newPage = l.attrs["href"]
					pages.add(newPage)
					print("#"),
					getLinks(newPage)
				except:
					continue

getLinks("qds.html")

for i in pages:
	nlink = urlopen("https://cdn.hackerrank.com/hackerrank/static/contests/capture-the-flag/infinite/"+i)
	nobj = BeautifulSoup(nlink, "html.parser")
	for item in nobj.findAll("font", {"color": "blue"}):
		t = item.get_text().strip("Secret Phrase: ")
		text.append(t)

text.sort()
for i in text:
	print(i)

