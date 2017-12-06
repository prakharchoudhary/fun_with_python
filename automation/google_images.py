import os
import sys
import time
import json
from pprint import pprint
from bs4 import BeautifulSoup
if sys.version_info[0:2] > (3, 0):
    from urllib.request import Request, urlopen
else:
    from urllib2 import Request, urlopen


class GoogleScraper(object):

    def __init__(self, search):
        self.search = ('%20').join(search.split(' '))
        self.headers = {}
        self.headers['User-Agent'] = \
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
        self.url = 'https://www.google.com/search?q={}&espv=2&biw=1366&bih=667&site=webhp&source=lnms&tbm=isch&sa=X&ei=XosDVaCXD8TasATItgE&ved=0CAcQ_AUoAg'.format(
            search)

    def get_soup(self, url, header):
        return BeautifulSoup(
            urlopen(Request(url, headers=self.headers)), 'html.parser')

    def _get_all_images(self):
        AllImages = []  # contains the link for Large original images, type of  image
        soup = self.get_soup(self.url, self.headers)
        for url in soup.find_all("div", {"class": "rg_meta"}):
            link, Type = json.loads(
                url.text)["ou"], json.loads(
                url.text)["ity"]
            AllImages.append((link, Type))
        return AllImages

    def write_images(self):
        k = 0
        errorCount = 0
        items = self._get_all_images()
        print("Total items: %s" % len(items))
        print("Starting Download...")
        for idx, (link, type) in enumerate(items):
            try:
                req = Request(link, headers=self.headers)
                img = urlopen(req, None, 15)
                output_file = open(self.search + "/" +
                                   str(k + 1) + ".jpg", 'wb')

                data = img.read()
                output_file.write(data)
                img.close()

                print("completed ====> " + str(k + 1))

                k = k + 1

            except IOError:  # If there is any IOError
                errorCount += 1
                print("IOError on image " + str(k + 1))
                k = k + 1


def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == '--search' or sys.argv[1] == '-S':
            searchFor = GoogleScraper(sys.argv[2])
            if not os.path.exists('./{}'.format(sys.argv[2])):
                os.mkdir('./{}'.format(sys.argv[2]))
    else:
        s = input("Enter the search keywords: ")
        searchFor = GoogleScraper(s)
        if not os.path.exists('./{}'.format(s)):
            os.mkdir('./{}'.format(s))

    searchFor.write_images()

if __name__ == '__main__':
    main()
