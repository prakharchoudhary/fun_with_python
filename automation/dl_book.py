'''
An automation script that automatically scapres all the contents of the
free DeepLearning book on DeepLearning.org and saves all of them in one pdf files.
'''

import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pdfkit
import os
import pprint

html = urlopen("http://www.deeplearningbook.org/")
obj = BeautifulSoup(html, "html.parser")

links = []

base_url = "http://www.deeplearningbook.org/"

li = obj.find_all("a", href=re.compile("contents/.+"))
for i in li:
	links.append(base_url + i["href"])

pprint.pprint(links)

pdfkit.from_url(links, "DLBook.pdf")
