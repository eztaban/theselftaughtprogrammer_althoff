import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        """
        :var r: Stoes HTML and data from self.site due to urlopen
        :var html: stores the HTML only due to the read() method
        :var parser: we are parsing html :)
        :var sp: BeautifulSoup does the hard work of parsing the HTML
        :sp.find_all("a"): finds all URLs since they are tagged <a>URL</a>
        :var url: stores the value of "href", which is the url itself
        
        """
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        urls = []
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                print("Nothing here")
                continue
            if "html" in url:
                print("\n" + url)
                urls.append(url)
        with open("headers.txt", "w") as f:
            for url in urls:
                f.write(url + "\n") 

news = "https://news.google.com"
#news = "https://hestehoej.dk/"
#news = "https://www.youtube.com/"
news = "https://books.toscrape.com/"
#news = "https://quotes.toscrape.com/" #nothing here
Scraper(news).scrape()
        
