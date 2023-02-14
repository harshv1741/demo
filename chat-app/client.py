#!/usr/bin/python3

# Importing Libraries
import socket
import select
import sys

from thread import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(server.SOL_SOCKET, socket.SO_REUSEADDR, 1)

if len(sys.argv) != 3:
    print ("Correct usage: script, IP address, port number")
    exit()

IP_address = str(sys.argv[1])
Port = int(sysv.argv[2])


server.bind((IP_address, Port))


server.listen(100)

list_of_clients = []


def clientthread(conn, addr):

    conn.send("---- Welcome to chatroom \"Godzilla\"! ----")

    while True:

        if msg:
            print("{"+addr[0]+"}"+ msg)

            msg_to_send = "{"+addr[0]+"}" 
