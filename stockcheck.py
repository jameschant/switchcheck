import schedule
import time

# freq = sched.scheduler()


def job():
    print("I'm working")

schedule.every(10).seconds.do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)


# - On a regular time interval...
# Make a GET request to a specific web page...
# Check for a string on that page...
# If that string is there take an action, like sending a text to my number....
# Ensure that once this happens the script is broken and it stops, unless of
# course I start it again when it's next out of stock

# You shouldn't need the Flask framework or anything, but you will likely need a
#  couple of key modules. Some might come with python3. You will need to run it
# somewhere that's always on.
