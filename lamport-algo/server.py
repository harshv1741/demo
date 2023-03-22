#!/usr/bin/python3
import socket
import threading
import time

# Set up server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8000))
server_socket.listen(1)

# Initialize clock and lock
clock = 0
lock = threading.Lock()

# Function to handle client connections
def handle_connection(conn, addr):
    global clock
    # Receive message from client
    msg = conn.recv(1024).decode()
    # Acquire lock and update clock
    with lock:
        clock += 1
        print(f"Received message '{msg}' from {addr} at time {clock}")
    # Send reply to client
    conn.send(f"Received message '{msg}'".encode())
    # Close connection
    conn.close()

# Listen for incoming connections
while True:
    conn, addr = server_socket.accept()
    # Start new thread to handle connection
    threading.Thread(target=handle_connection, args=(conn, addr)).start()
