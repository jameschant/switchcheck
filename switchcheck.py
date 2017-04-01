import schedule
import time
import re
import requests
from twilio.rest import TwilioRestClient


stock = False


print("Begin check")


def check():
    account_sid = ""
    auth_token = ""
    client = TwilioRestClient(account_sid, auth_token)
    page = requests.get('https://www.amazon.co.uk/Nintendo-UK-NSHEHWNIN45229-Switch-Grey/dp/B01MFADJFV/')
    html_contents = str(page.text)
    textonpage = re.findall('In Stock', html_contents)
    if len(textonpage) == 0:
        print("Item not in stock.")
    else:
        global stock
        stock = True
        print("Item in stock.")
        client.messages.create(
            to="",
            from_="",
            body="The Nintendo Switch is in stock on Amazon UK!")

# Set the time interval for check to run
schedule.every(5).minutes.do(check)


# Starting with the assumption there is no stock, run the check until there is
while stock is False:
    # Schedule a call of the check function
    # print("Running")
    schedule.run_pending()
    time.sleep(1)
