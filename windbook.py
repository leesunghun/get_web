#!/usr/bin/python

#-*- coding: utf-8 -*-


import urllib2
from BeautifulSoup import BeautifulSoup
import time

url = "http://www.goyanglib.or.kr/pung/data/dataBook.asp?a_v=&a_lib=ML&a_cp=" 
list_url="http://sglib.mapo.go.kr/data/new_book_list.asp?table_name=new_book"
move_url="http://sglib.mapo.go.kr/data/new_book_list.asp?page1="

f=urllib2.urlopen(url)
page=f.read()
f.close()

soup=BeautifulSoup(page)
print soup
