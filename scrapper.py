import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL ="https://www.amazon.in/HP-x740w-Flash-Drive-Gray/dp/B075B46XCG/ref=sr_1_12?crid=BJ4261Z0HIFD&keywords=pendrive+32gb+offers+today+low+price+best&qid=1562348869&s=gateway&sprefix=pendr%2Caps%2C282&sr=8-12"
#the url belongs to the product i am planning to buy
headers = {"User-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}
def check_price():
        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        title = soup.find(id= "productTitle").get_text() 
        price = soup.find(id= "priceblock_ourprice").get_text() 
        converted_price = float(price[1:6])

        if(converted_price < 500):
            send_mail()

        print(title.strip())
        print(converted_price)

        if(converted_price < 500): #the price is based on my product that ive choosed
            send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('','') #Add your mail username and password inside the quotes

    subject = "Hey, Prasanth ! The Price fell down"
    body = 'Check the link https://www.amazon.in/HP-x740w-Flash-Drive-Gray/dp/B075B46XCG/ref=sr_1_12?crid=BJ4261Z0HIFD&keywords=pendrive+32gb+offers+today+low+price+best&qid=1562348869&s=gateway&sprefix=pendr%2Caps%2C282&sr=8-12  '

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        '',
        '',
        msg
    ) #put your from mail id and to mail id within the quotes 
    print("Hey the mail has been sent")
    
    server.quit()
while(True):

    check_price()
    time.sleep(60 * 60)