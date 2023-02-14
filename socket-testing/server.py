#!/usr/bin/python3

import socket

# Creating a socket object.
s = socket.socket()

# Reserving a port
port = 12345

# Bind to the port
s.bind(('', port))
print ("Socket binded to %s" %(port))

# put the socket into listening mode 
s.listen(5)
print ("Socket is listening")

# A forever loop untill an interrupt occurs
while True:

    # Establish connection with client
    c, addr = s.accept()
    print('Got connection from', addr )

    # Sending a message to the client. encoding to send byte type.
    c.send('Thank You for connecting'.encode())

    # Close the connection with the client
    c.close()

    # Breaking once the connection is closed
    break
