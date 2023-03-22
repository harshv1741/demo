#!/usr/bin/python3
import socket
import threading
import time

# Set up client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8000))

# Initialize clock and lock
clock = 0
lock = threading.Lock()

# Function to send message to server
def send_message(msg):
    global clock
    # Acquire lock and update clock
    with lock:
        clock += 1
        # Send message to server
        client_socket.send(msg.encode())
        # Receive reply from server
        reply = client_socket.recv(1024).decode()
        print(f"Received reply '{reply}' at time {clock}")

# Send some test messages
send_message("Hello")
send_message("World")
send_message("Lamport")
