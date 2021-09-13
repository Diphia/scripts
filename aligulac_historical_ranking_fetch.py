import requests
from bs4 import BeautifulSoup

ratings=[]
dates=[]

current_player_link = 'http://aligulac.com/players/15-HyuN/historical/'
response = requests.get(current_player_link)
soup = BeautifulSoup(response.text, features='html.parser')

#for rating in soup.find_all('td',attrs={'class':'rl_rating'}):
    #ratings.append(int(rating.string))

m = soup.find_all('div',attrs={'class':'col-lg-12 col-md-12 col-sm-12 col-xs-12'})
print(m.h2)



#print(ratings)
