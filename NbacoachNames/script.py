import pandas
from bs4 import BeautifulSoup
import requests


player = []
number = []
position = []
height = []
Team = []

linkjoined = []
url = 'http://www.nba.com/news/coaches/index.html?ls=iref:nba:gnav'
request = requests.get(url)
soup = BeautifulSoup(request.text, 'lxml')
links = soup.select("#block-teamlistblock a")
for l in links:
    linkjoined.append("https://www.nba.com"+l['href'])

for lj in linkjoined[1:]:
    request2 = requests.get(lj)
    soup2 = BeautifulSoup(request.text, "lxml")
    names = soup2.findAll(class_="nba-player-index__name")
    positions = soup2.select(".nba-player-index__details span:nth-child(1)")
    details = soup2.select(".nba-player-index__details span+ span")
    numbers = soup2.find_all(class_="nba-player-trending-item__number")
    for d in details:
        height.append(d.text)
    for n in names:
        player.append(n.text)
    for p in positions:
        position.append(p.text)
    for n in numbers:
        number.append(n.text)	


Data = pandas.DataFrame({
    "Player":player,
    "Number":number,
    "Position":position,
    "Height":height,
})
Data.to_csv("NBAplayers.csv")


