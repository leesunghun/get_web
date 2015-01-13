# -*- coding: cp949 -*-
import urllib2
from BeautifulSoup import BeautifulSoup
import time

url = "http://sglib.mapo.go.kr/data/new_book_view.asp?table_name=new_book&method=view&val_01="
list_url="http://sglib.mapo.go.kr/data/new_book_list.asp?table_name=new_book"
move_url="http://sglib.mapo.go.kr/data/new_book_list.asp?page1="


def change_word(word):
    if word:
        word1=word.replace("&nbsp;","")
        word2=word1.replace("&middot","")
    else:
        word2="none"
    return word2

def print_booklist(number):

    print number
 #   print number
    for count in range(1000, 1822):
        time.sleep(2)
        urls= url + `count`
     
        num=1
        f = urllib2.urlopen(urls)
        page = f.read().decode('cp949', 'ignore')
        f.close()

        soup = BeautifulSoup(page, fromEncoding="euc-kr")
        #rows= soup.findAll('tr', {'height': '24'})
        rows= soup.findAll('tr')

 # 여기 까지는 한글 파일이 저장이 된다.               
                
        for item in rows[1:]:
                tdata=item.findAll('td')
                ctype=0
                dot=","
                wword=str(count) + dot
                
                for akdata in tdata:
                    ctype = ctype+1
                    book_line=change_word(akdata.text)
                    bn=unicode(book_line).encode('cp949')
                    wword=wword + dot +bn
                wword= wword + "\n"    
                file_data=wword    
                print file_data

                    
                """    
                위 라인에 중복되는것을 재귀로 다시 풀었다.
                
                book_num=tdata[0].text
                bn=unicode(book_num).encode('cp949')
                book_title=change_word(tdata[1].text)
                bt=unicode(book_title).encode('cp949')
                book_pin=change_word(tdata[2].text)
                bp=unicode(book_pin).encode('cp949')
                dot=","
                cn=count 
                print "%d  %s %d %s %s %s %s \n" % (cn,dot,num,dot,bt,dot,bp)
                file_data="%d  %s %d %s %s %s %s \n" % (cn,dot,num,dot,bt,dot,bp)
                """           
               
                with open("bookdata\\"+`count`+".txt",'a') as f:
                    f.write(str(file_data))
                
            
                num=num+1
                
        print count
        f.close()
    print "all done"
        
def get_last_number():
        f = urllib2.urlopen(list_url)
        page = f.read().decode('cp949', 'ignore')
        f.close()

        soup = BeautifulSoup(page)
        rows= soup('tr')
        for link in rows[1:2]:
                data=link.find('a')['href']
        num_data=data.split("&")
        num_data1=num_data[2].replace("val_01=","")
        last_number=int(num_data1)
        print_booklist(last_number)

        


get_last_number()
