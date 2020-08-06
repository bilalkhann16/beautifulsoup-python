from bs4 import BeautifulSoup
import requests

page=requests.get('https://forecast.weather.gov/MapClick.php?lat=34.0536&lon=-118.2455#.XyqOpxlRVxA')
soup=BeautifulSoup(page.content,'html.parser')

week=soup.find(id='current-conditions-body')
items=week.find(class_='myforecast-current-lrg').get_text()
print (items)