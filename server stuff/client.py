# client.py
from time import sleep
import socket                          # Import socket module

s = socket.socket()                    # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 60000                           # Reserve a port for your service.

##c = socket.socket()
##c.connect((host, port))

s.connect((host, port))
s.send(b"Hello server!")

recieving_file = s.recv(1024)

with open('recieving_file.cpp', 'wb') as f:
    print ('file opened')
    while True:
        print('receiving data...')
        data = s.recv(1024)
        print('data={}'.format (data))
        if not data:
            break
        # write data to a file
        f.write(data)

f.close()
print('Successfully get the file')
s.close()
print('connection closed')

sleep(5)
