import os
import requests
from bs4 import BeautifulSoup
from twilio.rest import Client 
from sender import *

# The page that we getting the information about the project 
# Storing it in the url variable 

def get_price():
    url ="https://www.amazon.in/ZOTAC-GeForce-256-bit-Graphics-ZT-T20610D-10P/dp/B07TWGRW5H/ref=sr_1_2?dchild=1&keywords=rtx+2060+super&qid=1588862502&sr=8-2"

    headers ={"User-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}

    # This will return the data from the website
    page = requests.get(url,headers=headers)

    soup = BeautifulSoup(page.content,'html.parser')

    # Getting products value from amazon.in's id and removing excess element info
    price_online =  soup.find(id="priceblock_ourprice").get_text()

    # Converting our string value to float 
    price_converted= float((price_online[2:8]).replace(',',''))
    
    # Getting tht complete name of the product
    product_title= soup.find(id ="productTitle").get_text().strip()
    
    print(price_converted)
    print(product_title)
    

    def updater():
        """
        This method takes the converted price from the above method and send the appropriate message.
        The message is sent to the contact number using twilio API.
        """
        # From the command line, set environment variables to contain your credentials.
        # Your Account Sid and Auth Token from twilio.com/user/account
        client = Client() 
        
        if price_converted<36000:
            msg = f'Price has fallen for {product_title} it is going for {price_converted} rs now.'
        else:
            msg = f"Today's rate for {product_title} is {price_converted} rs now."
        
        message = client.messages.create( 
                                from_= 'whatsapp:+14155238886',  
                                body= msg,      
                                to='whatsapp:+919892634021') 
 
        print(message.sid)
        print("Message sent")

    updater()

get_price()