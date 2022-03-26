#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

link = 'https://aqicn.org/city/australia/nsw/kembla-grange/illawarra'

response = requests.get(link)
#print(response.content)
soup = BeautifulSoup(response.text, features='html.parser')
print(soup)

#m = soup.find_all('div', attr={'class':'history-aqidata-block'})
#m = soup.find_all('div', attr={'class':'h1section'})
