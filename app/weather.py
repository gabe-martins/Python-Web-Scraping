import requests
from bs4 import BeautifulSoup

def scraping(base_url):
  req = requests.get(base_url)
  soup = BeautifulSoup(req.content, 'html.parser')
  return soup

scraping('https://www.climatempo.com.br/previsao-do-tempo/cidade/332/voltaredonda-rj')
