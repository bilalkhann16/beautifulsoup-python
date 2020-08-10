from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession
session = HTMLSession()
resp = session.get("https://www.amazon.com/Sceptre-E248W-19203R-Monitor-Speakers-Metallic/dp/B0773ZY26F/ref=sr_1_2?crid=1861TM8A5NDPX&dchild=1&keywords=monitors&qid=1597071906&sprefix=monitors%2Caps%2C364&sr=8-2")
resp.html.render()
soup = BeautifulSoup(resp.html.html, "lxml")
title = soup.find(id = "productTitle").get_text().strip()
print (title)
