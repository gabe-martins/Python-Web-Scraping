import requests
from bs4 import BeautifulSoup


def scraping(base_url):
  req = requests.get(base_url)
  soup = BeautifulSoup(req.content, 'html.parser')
  return soup

link = 'https://www.climatempo.com.br/previsao-do-tempo/cidade/332/voltaredonda-rj'

print(scraping(link).find(class_ = '-gray -line-height-24 _center').text)

def weather(city):
  req = requests.get(city)
  soup = BeautifulSoup(req.content, 'html.parser')

  print('Resumo: ' + soup.find(class_ = '-gray -line-height-24 _center').text)
  print('Máximas: ' + soup.find(id = 'max-temp-1').string)
  print('Mínimas: ' + soup.find(id = 'min-temp-1').string)

weather(link)