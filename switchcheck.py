import schedule
import time
from urllib.request import urlopen
import re
# from twilio.rest import TwilioRestClient

stock = False

site = urlopen('https://www.amazon.co.uk/Nintendo-UK-NSHEHWNIN45229-Switch-Grey/dp/B01MFADJFV/').read()
textonpage = re.findall(b'In Stock.', site)
# client = TwilioRestClient("XX", "YY")


def check():
    if len(textonpage) == 0:
        print("Not there.")
    else:
        global stock
        stock = True
        print("It's in stock.")
        # If that string is there send a text to my number
        # client.messages.create(to="XX", from_="YY", body="The Nintendo Switch is in stock on Amazon UK!")


# Set the time interval to run on 
schedule.every(20).seconds.do(check)


# If there is no stock, run the check until there is.
while stock == False:
    print("Running")
    schedule.run_pending()
    time.sleep(1)