import schedule
import time
import re
import requests
from twilio.rest import TwilioRestClient


stock = False


print("Begin check")


def check():
    account_sid = "AC542e629143b6f86ab8b0c92b01fbfbfd"
    auth_token = "81b095f826a95ace93ab28257e5b9aa6"
    client = TwilioRestClient(account_sid, auth_token)
    f = requests.get('https://www.amazon.co.uk/Nintendo-UK-NSHEHWNIN45229-Switch-Grey/dp/B01MFADJFV/')
    site = f.text
    textonpage = re.findall(b'In Stock', site)
    if len(textonpage) == 0:
        print("Item not in stock.")
    else:
        global stock
        stock = True
        print("Item in stock.")
        client.messages.create(
            to="+447796896439",
            from_="+441304410174",
            body="The Nintendo Switch is in stock on Amazon UK!")

# Set the time interval for check to run
schedule.every(2).minutes.do(check)


# Starting with the assumption there is no stock, run the check until there is
while stock is False:
    # Schedule a call of the check function
    # print("Running")
    schedule.run_pending()
    time.sleep(1)
