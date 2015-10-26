#!/usr/bin/python

import urllib2
from bs4 import BeautifulSoup

#base_url="http://www.goyanglib.or.kr/pung/data/dataBook.asp"

base_url="http://www.goyanglib.or.kr/pung/data/dataBook.asp?a_q=&a_dm=9&a_dy=2015&a_lib=ML&a_cp=8"

response=urllib2.urlopen(base_url)
get_html=response.read()

soup = BeautifulSoup(get_html, 'html.parser')

data=soup.findAll('div', attrs={'class':'fl'})

print "-"*20

for get_value in data:
    for d_data in get_value.find_all('p'):
        print d_data.text
    print "-"*20
