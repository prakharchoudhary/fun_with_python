import os
import sys
import time
import json
import threading
from pprint import pprint
from bs4 import BeautifulSoup
if sys.version_info[0:2] > (3, 0):
    from urllib.request import Request, urlopen
else:
    from urllib2 import Request, urlopen


class GoogleScraper(object):

    def __init__(self, search, keywords=None):
        self.search = ('%20').join(search)
        if keywords:
            self.keywords = ('+').join(keywords)
        self.headers = {}
        self.headers['User-Agent'] = \
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
        if not keywords:
            self.url = 'https://www.google.com/search?q={}&espv=2&biw=1366&bih=667&site=webhp&source=lnms&tbm=isch&sa=X&ei=XosDVaCXD8TasATItgE&ved=0CAcQ_AUoAg'.format(
                self.search)
        else:
            self.url = 'https://www.google.com/search?q={},g_2={}&espv=2&biw=1366&bih=667&site=webhp&source=lnms&tbm=isch&sa=X&ei=XosDVaCXD8TasATItgE&ved=0CAcQ_AUoAg'.format(
                self.search, self.keywords)
        print(self.url)
        self.k = 0
        self.errorCount = 0

    def get_soup(self):
        return BeautifulSoup(
            urlopen(Request(self.url, headers=self.headers)), 'html.parser')

    def _get_all_images(self):
        AllImages = []  # contains the link for Large original images, type of  image
        soup = self.get_soup()
        for url in soup.find_all("div", {"class": "rg_meta"}):
            link, Type = json.loads(
                url.text)["ou"], json.loads(
                url.text)["ity"]
            AllImages.append((link, Type))
        return AllImages

    def _write_images(self, items, start, end):
        for idx, (link, type) in enumerate(items[start:end]):
            try:
                req = Request(link, headers=self.headers)
                img = urlopen(req, None, 15)
                try:
                    output_file = open((' ').join(self.search.split('%20')) + "/" +
                                       str(self.k + 1) + ".jpg", 'wb')
                    data = img.read()
                    output_file.write(data)
                except Exception as e:
                    print(e)
                img.close()

                print("completed ====> " + str(self.k + 1))

                self.k = self.k + 1

            except IOError:  # If there is any IOError
                self.errorCount += 1
                print("IOError on image " + str(self.k + 1))
                self.k = self.k + 1

            except Exception as e:
                self.errorCount += 1
                print(e)
                self.k = self.k + 1

    def write_all_images(self):
        items = self._get_all_images()
        print("Total items: %s" % len(items))
        print("Starting Download...")
        downloadThreads = []                # a list of all the Thread objects
        for i in range(0, len(items), int(len(items) / 10)):
            downloadThread = threading.Thread(
                target=self._write_images, args=(items, i, i + 10))
            downloadThreads.append(downloadThread)
            downloadThread.start()

        for downloadThread in downloadThreads:
            downloadThread.join()

        print("\nImages Downloaded!")
        print("Error Count: %s" % (self.errorCount))


def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == '--search' or sys.argv[1] == '-S':
            searchFor = GoogleScraper(sys.argv[2:])
            dirname = (' ').join(sys.argv[2:])
            if not os.path.exists('./{}'.format(dirname)):
                os.mkdir('./{}'.format(dirname))
    else:
        s = input("Enter the search term: ").split(' ')
        searchFor = GoogleScraper(search=s)
        if not os.path.exists('./{}'.format(s)):
            os.mkdir('./{}'.format(s))

    searchFor.write_all_images()

if __name__ == '__main__':
    main()
