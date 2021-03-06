# server.py
from time import sleep
import socket                   # Import socket module

from tkinter import Tk
from tkinter.filedialog import askopenfilename

def folder_finder_gui():
    Tk().withdraw()                       # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    return filename

port = 60000                             # Reserve a port for your service.
s = socket.socket()                     # Create a socket object
host = socket.gethostname()      # Get local machine name
s.bind((host, port))                    # Bind to the port
s.listen(5)                                 # Now wait for client connection.

print ('Server listening....')

while True:
    conn, addr = s.accept()     # Establish connection with client.
    print ('Got connection from', addr)
    data = conn.recv(1024)
    print('Server received', repr(data))

    filename = folder_finder_gui()
    conn.send(filename.encode())
    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
       conn.send(l)
       print('Sent ',repr(l))
       l = f.read(1024)
    f.close()

    print('Done sending')
    # Figure out ways to shut this thing down 
    #conn.send(b'Thank you for connecting')
    conn.shutdown(socket.SHUT_WR)

sleep(5)
