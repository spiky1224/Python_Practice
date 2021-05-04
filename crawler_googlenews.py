import urllib.request
from bs4 import BeautifulSoup

class Scraper:
  def __init__(self, site):
    self.site = site
  
  def scrape(self):
    r = urllib.request.urlopen(self.site)
    html = r.read()
    parser = "html.parser"
    sp = BeautifulSoup(html, parser)
    for tag in sp.find_all("a"):
      url = tag.get("href")
      print(url)
      if url is None:
        continue
      #if url[:-5] == '.html':
      #if url.endswith('.html'):
      if "html" in url:
        print('\n' + url)

news = "https://news.google.com/"
Scraper(news).scrape()