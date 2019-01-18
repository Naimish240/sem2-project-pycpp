# reads contents of the file
from time import sleep

fh = open('received_file.txt','r')

for i in fh.readline():
    print(i)

fh.close()

sleep(5)
