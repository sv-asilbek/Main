# import pygeoip
# import requests
#
# my_ip_address = requests.get('http://95.130.227.174').text
# gip = pygeoip.GeoIP('GeoLiteCity.dat')
# res = gip.record_by_addr(my_ip_address)
#
# print(my_ip_address)

# !/usr/bin/env python2
import requests
from bs4 import BeautifulSoup
import pynotify
from time import sleep


def sendmessage(title, message):
    pynotify.init("Test")
    notice = pynotify.Notification(title, message)
    notice.show()
    return


url = "http://static.cricinfo.com/rss/livescores.xml"
while True:
    r = requests.get(url)
    while r.status_code is not 200:
        r = requests.get(url)
    soup = BeautifulSoup(r.text)
    data = soup.find_all("description")
    score = data[1].text
    sendmessage("Score", score)
    sleep(60)
