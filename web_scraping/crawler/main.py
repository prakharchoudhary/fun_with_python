import threading
import queue
from Crawler import *

def main():
	print("Starting our Web Crawler")
	baseUrl = input("Website > ")
	numberOfThreads = input("No Threads > ")

	linksToCrawl = queue.Queue()
	urlLock = threading.Lock()
	linksToCrawl.put(baseUrl)
	haveVisited = []
	crawlers = []
	errorLinks = []

	with open("links.txt", "w+") as f:
		for i in range(int(numberOfThreads)):
			crawler = Crawler(baseUrl, linksToCrawl, haveVisited, errorLinks, urlLock, f)
			crawler.run()
			crawlers.append(crawler)
		
		for crawler in crawlers:
			crawler.join()

	print("Total Number of Pages Visited {}".format(len(haveVisited)))
	print("Total Number of Pages with Errors {}".format(len(errorLinks)))

if __name__ == '__main__':
	main()