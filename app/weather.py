import sys

sys.path.insert(0, './src')
from goToWeb import ScrapingWeb

def setUp(self, url):
  self.url = url
  self.goToWeb.get_soup(self.url)


clima = setUp()
clima.setUp('https://www.climatempo.com.br/previsao-do-tempo/cidade/332/voltaredonda-rj')