import requests
from time import sleep
from bs4 import BeautifulSoup
from sms import send_sms

user = "USER2"
test = False

# Other bike:
if test:
    url1 = "https://www.canyon.com/en-us/outlet-bikes/road-bikes/endurace-cf-slx-disc-8.0-etap/2398.html"
else:
    url1 = "https://www.canyon.com/en-us/outlet-bikes/road-bikes/speedmax-cf-slx-8-disc-di2/2572.html"

url2 = "https://www.canyon.com/en-us/road-bikes/triathlon-bikes/speedmax/cfr/speedmax-cfr-disc-etap/3065.html"


def ping(url):
    available = False

    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    status = [
        x.text for x in soup.find_all(
            "div", class_="productConfiguration__availabilityMessage")
    ]

    size = [
        x.text for x in soup.find_all(
            "div",
            class_=
            "productConfiguration__variantType js-productConfigurationVariantType"
        )
    ]

    noti = ""
    i = 0
    for s in status:
        if "Coming soon" in s:
            noti += size[i].replace(" ", "").replace("\n", "") + " : NA"
        else:
            noti += size[i].replace(" ", "").replace("\n", "") + " : A"
            available = True
        noti += "\n"
        i += 1

    return noti, available


def notify(noti):
    if user == "USER1":
        number = "1234567890"
        provider = "AT&T"
    elif user == "USER2":
        number = "0987654321"
        provider = "Verizon"
    elif user == "USER3":
        number = "1357924680"
        provider = "AT&T"

    message = noti
    sender_credentials = ("USER", "TOKEN")
    send_sms(number, message, provider, sender_credentials)


def main():
    if test:
        noti = "Endurace CF SLX Disc 8.0 eTap\n"
    else:
        noti = "Speedmax CF SLX 8 Disc Di2\n"
    p1 = ping(url1)
    noti += p1[0]
    noti += "\nSpeedmax CFR Disc eTap\n"
    p2 = ping(url2)
    noti += p2[0]
    if p1[1] or p2[1]:
        notify(noti)
    else:
        print("NA")

while True:
    main()
    sleep(300)
