import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.in/Apple-iPhone-Pro-Max-256GB/dp/B07XVLH744/ref=sr_1_1_sspa?crid=2VCKZNOH3H6SR&keywords=apple+iphone+11+pro+max&qid=1582043410&sprefix=apple+iphone%2Caps%2C388&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyVjdZSE83TzU4UUMmZW5jcnlwdGVkSWQ9QTAyNTI1ODZJUzZOVUwxWDNIUlAmZW5jcnlwdGVkQWRJZD1BMDkxNDg4MzFLMFpVT1M5OFM5Q0smd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl"

headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0"}

page = requests.get(url, headers=headers)
print(page.status_code)

soup = BeautifulSoup(page.content, "html.parser")

#print(soup.prettify()) 

title = soup.find(id = "productTitle")
if title:
    title = title.get_text()
else:
    print ("Hello I am")
    title = "default_title"

price = soup.find(id = "priceblock_ourprice").get_text()

converted_price = price[0:8]

print(converted_price)
print(title)
