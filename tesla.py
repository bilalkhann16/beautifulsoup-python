from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession
import smtplib
from smtplib import SMTP

def sendemail1():
    try:
        server= smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.ehlo()
        tdcdcefmrbstzjif
        server.login('lalbikhan2014@gmail.com', 'tdcdcefmrbstzjif')   #Email address from which you want to send email
        subject="Tesla Price Alert"
        body="Tesla Stock Price just hit the targeted price. Thanks! "
        msg = f"Subject:{subject}\n\n{body}"
        server.sendmail( 'lalbikhan2014@gmail.com',
        'bilal.khan2014@hotmail.com',
        msg)
        print ("I'm here")
    except:
        print ("Error in sending email")

    print ('\nEmail sent success\n')
    server.quit()


def check_price():
    page = requests.get("https://finance.yahoo.com/quote/TSLA/")
    soup = BeautifulSoup(page.content, "lxml")
    title = soup.find(class_ = "D(ib) Fz(18px)").get_text()
    price= soup.find(class_ = "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)").get_text()
    floatprice=float(price[0:5])

    print ("Title: ",title)
    print("Price:", floatprice)
    if (floatprice < 400):
        print("Hello World")
        sendemail1()
check_price()
