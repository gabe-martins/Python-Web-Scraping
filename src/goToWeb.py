import requests
from bs4 import BeautifulSoup

#web scraping
class ScrapingWeb:

  def __init__(self, url):
    self.url = url
    self.req = requests.get(self.url)
    self.soup = BeautifulSoup(self.req.content, 'html.parser')

  def get_soup(self):
      return self.soup

  def get_html(self):
    return self.soup.findAll()
    