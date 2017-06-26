"""
Download all the comics from xkcd comics
"""

#!/usr/bin/python3
# xkcddownloader.py - Downloads every single XKCD comic.

import requests, os, bs4

url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True) #creates a new dir 'xkcd'
								   # if it doesnot exist

while not url.endswith('#'):
	#TODO: Download the page
	print('Downloading page %s....' % url)
	res = requests.get(url)
	res.raise_for_status()

	soup = bs4.BeautifulSoup(res.text, 'lxml')
	#TODO: Find url to next page

	comicElem = soup.select('#comic img')
	if comicElem == []:
		print("Could not find comic image.")
	else:
		comicUrl = 'http:' + comicElem[0].get('src')
		#TODO : Download the image
		print('Downloading page %s....' % comicUrl)
		res = requests.get(comicUrl)
		res.raise_for_status()


	#TODO: Save the image to ./xkcd
	imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
	for chunk in res.iter_content(100000):
		imageFile.write(chunk)
	imageFile.close()

	#TODO: Get the Prev button's url
	prevLink = soup.select('a[rel=prev]')[0]
	url = 'http://xkcd.com' + prevLink.get('href')

print('Done.')

