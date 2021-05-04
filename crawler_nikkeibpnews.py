import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup as BS

class Scraper:
  def __init__(self, site):
    self.site = site
    self.urls = set()
  
  def scrape(self):
    r = urllib.request.urlopen(self.site)
    html = r.read()
    parser = 'html.parser'
    sp = BS(html, parser)
    for tag in sp.find_all('a'):
      url = tag.get('href')
      if url is None:
        continue
      if 'atcl/contents' not in url:
        continue
      full_url = urljoin(r.url, url)
      if full_url in self.urls:
        continue
      self.urls.add(full_url)
      print('\n' + full_url)

news = 'https://xtrend.nikkei.com/atcl/contents/new/'
Scraper(news).scrape()