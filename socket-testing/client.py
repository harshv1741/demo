#!/usr/bin/python3

# Import Socket Module 
import socket

s = socket.socket()

# Define the port on which you want to connect
port = 12345

# Connect Server to local Computer
s.connect(('127.0.0.1', port))

# receive data from the server and decoding to get the string.
print(s.recv(1024).decode())

# close the connection
s.close()
