도서관 리스트 가져오는 프로그램2
 -*- coding: utf-8 -*-
'''
도서관에서 신규도서 목록 가져와서 보기
마지막 변경:2014-10-06
'''

import urllib2
from BeautifulSoup import BeautifulSoup
import time

url = "http://sglib.mapo.go.kr/data/new_book_view.asp?table_name=new_book&method=view&val_01="
list_url="http://sglib.mapo.go.kr/data/new_book_list.asp?table_name=new_book"
move_url="http://sglib.mapo.go.kr/data/new_book_list.asp?page1="

def change_word(word):
    word1=word.replace("&nbsp;","")
    word2=word1.replace("&middot","")
    return word2


def print_booklist(data_min,data_max):
    num=1
    for count in range(data_min,data_max):


        urls= url + `count`


        f = urllib2.urlopen(urls)
        page = f.read().decode('cp949', 'ignore')
        f.close()

        soup = BeautifulSoup(page)
        rows= soup.findAll('tr', {'height': '18'})
        f = file(`count`, 'wb')

        for item in rows:
                a=item.findAll('td')
                book_num=a[1].text
                book_title=change_word(a[2].text)
                book_user=change_word(a[3].text)
                book_store=a[4].text
                print num,book_num,book_title,book_user,book_store
            
                num =num +1
        f.close()

       
def print_newbook():

        f = urllib2.urlopen(list_url)
        page = f.read().decode('cp949', 'ignore')
        f.close()

        soup = BeautifulSoup(page)
        rows= soup.findAll('tr')

        num_list=[]
        for item in rows:
                a=item.findAll('td')
         
                for c in a[0:1]:
                        d=c.text
                        dd=d.replace("&nbsp;","")
                        d3=dd.replace("&middot","")
       
                        num_list.append(int(d3))

                print ' '
                for c in a:
                        d=c.text
                        dd=d.replace("&nbsp;","")
                        d3=dd.replace("&middot","")

                        print d3 + "   |" ,

                print ' '

        data_max=max(num_list)
        data_min=min(num_list)
        f.close()
        print_booklist(data_min,data_max)
def print_allbook():

    for  add_num in range(1,10):
            time.sleep(2)
            get_url=move_url + `add_num`
            f = urllib2.urlopen(get_url)
            page = f.read().decode('cp949', 'ignore')
            f.close()

            soup = BeautifulSoup(page)
            rows= soup.findAll('tr')

            num_list=[]
            for item in rows:
                    a=item.findAll('td')
                    for c in a:
                            d3=change_word(c.text)
                            print d3 + "   |" ,

                    print ' '

            f.close()
     
print_allbook()
#print_booklist(1790,1792)
#print_newbook()
