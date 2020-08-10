from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession
import smtplib
from smtplib import SMTP

def check_price():
    session = HTMLSession()
    resp = session.get("https://www.amazon.com/Bluetooth-Earphones-Headphones-Auto-Pair-Definition/dp/B07ZYFWBC6/ref=sr_1_2?dchild=1&keywords=qcy+t5&qid=1596538146&sr=8-2")
    resp.html.render()
    soup = BeautifulSoup(resp.html.html, "lxml")
    title = soup.find(id = "productTitle").get_text().strip()
    price= soup.find(id = "priceblock_ourprice").get_text().strip()
    floatprice=float(price[1:6])

    print ("Title: ",title)
    print("Price:", floatprice)
    if (floatprice < 18):
        sendemail1()
        
def sendemail1():
    try:
        server= smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login('from email here', 'App password here')   #Email address from which you want to send email
        subject="Price down alert"
        body="Test Check of price."
        msg = f"Subject:{subject}\n\n{body}"
        server.sendmail( 'from email here',
        'to email here',
        msg)
    except:
        print ("Error in sending email")

    print ('\nEmail sent success\n')
    server.quit()
check_price()

