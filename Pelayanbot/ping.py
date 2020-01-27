import urllib.request
import time
 
 
def ping():
    data = urllib.request.urlopen("pelayanbot-mfd7.rhcloud.com").read()
    return data
 
while True:
    ping()
    print("ping")
    time.sleep(600)
