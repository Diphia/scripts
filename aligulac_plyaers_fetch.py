import requests
from bs4 import BeautifulSoup

players_link=[]

for i in range(280,283):
    current_rank_link = 'http://aligulac.com/periods/'+str(i)+'/'
    response = requests.get(current_rank_link)
    soup = BeautifulSoup(response.text, features='html.parser')
    count=0

    for players in soup.find_all('td',attrs={"class":"rl_name"}):
        players_link.append(players.a.get('href'))
        count+=1
        if(count==15):
            break

    print(str(i)+'  DONE')

players_link = list(set(players_link))

for link in players_link:
    print(link)
