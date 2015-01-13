import os
for root, dirs ,files in os.walk('c:/python/bookdata'):
     for file in files:
            print file
            f=open("c:/python/bookdata/"+file,'r')
            line = f.readlines()
            f.close()
            line[1]=""

            c=open("c:/python/bookdata/"+file,'w')
            num=0
            c.writelines(line)

            c.close()