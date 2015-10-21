#!/usr/bin/python

import urllib2

from bs4 import BeautifulSoup
base_url="http://www.goyanglib.or.kr/pung/data/dataBook.asp"
#get_html="<div class="resultBox">"
#get_page="<div id='page'>"
#split_book="<div class="fl" style="width:84%">"
#delete_word="amp"
response=urllib2.urlopen(base_url)
get_html=response.read()

soup = BeautifulSoup(get_html, 'html.parser')
#print(soup.prettify())

#data_html=soup.find_all('p')
#print data_html
#soup=BeautifulSoup(data_html,'html.parser')

#print(soup.get_text())

data=soup.findAll('div', attrs={'class':'fl'})
# title = cartoons[0].find('a').text
#new_data=data[1]
#for text in new_data:
#    value1=new_data.find('p').text
#    print value1

#print data[0].find('p').text

print "-"*20
#for  get_value in data[0]:
    #new_value=get_value.find('p')
#    print get_value.find('p').text 

for get_value in data:
    for d_data in get_value.find_all('p'):
        print d_data.text
    print "-"*20
