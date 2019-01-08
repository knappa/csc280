#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
from datetime import date
import csv
import platform

page = requests.get('http://www2.montgomerycountymd.gov/CCJurors/call_in_information.asp')

if page.status_code != requests.codes.ok:
    print("connection error")
    exit()

soup = BeautifulSoup(page.text, 'html.parser')

highlighted_elements = soup.select("font[color=#FF0000]")

jury_date_string = highlighted_elements[0].contents[0].split('\n')[0].strip()
jury_date_list = jury_date_string.split('/')
jury_date_list = (jury_date_list[2], jury_date_list[0], jury_date_list[1])

jury_date = date(*map(int,jury_date_list))

try:
    max_juror = int(highlighted_elements[2].contents[0])
except:
    max_juror = "NONE"

with open(r'/home/knappa/Dropbox/juror_numbers-%s.csv' % platform.node(), 'a') as file:
    writer = csv.writer(file)
    writer.writerow([jury_date,max_juror])
