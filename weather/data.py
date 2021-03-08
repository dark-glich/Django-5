from bs4 import BeautifulSoup
import requests

def weather_search(location):
    search = f'weather in {location}'
    url = f'https://www.google.com/search?q={search}'
    
    req = requests.get(url)
    data = BeautifulSoup(req.text, 'html.parser')
    update = data.find("div", class_='BNeawe').text
    return update
