import requests
from bs4 import BeautifulSoup
page=requests.get('https://forecast.weather.gov/MapClick.php?lat=34.0536&lon=-118.2455#.XyqOpxlRVxA')
soup=BeautifulSoup(page.content,'html.parser')
week=soup.find(id='seven-day-forecast-body')
print ("\nHello I am here")
print (week)
items=week.find_all(class_='tombstone-container')
print ("\nNow I am here")
print (items[0])
q1=items[0].find(class_="period-name").get_text()
print ("\nq1 here")
print (q1)
q2=items[0].find(class_="short-desc").get_text()
print ("\nq2 here")
print (q2)
q3=items[0].find(class_="temp").get_text()
print ("\nq3 here")
print (q2)

print("/nNow here")
period_name=[item.find(class_='period-name').get_text() for item in items]
short_des=[item.find(class_='short-desc').get_text() for item in items]
temp=[item.find(class_='temp').get_text() for item in items]
print(period_name)
print(short_des)
print (temp)
