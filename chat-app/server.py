import socket
import threading

# Connection Host
host = '127.0.0.1'
port = 55555

# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# List for Clients and their Nicknames
clients = []
nicknames = []


# Sending Message to all connected clients
def broadcast(message):
    for client in clients:
        client.send(message)

# Handling messages from clients
def handle(client):
    while True:
        try:
            # Broadcasting Message
            message = client.recv(1024)
            broadcast(message)

        except:
            # Removing and closing clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast("{} left!".format(nickname).encode('ascii'))
            nicknames.remove(nickname)
            break

# Listening function
def receive():
    while True:
        # Accept Connection
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        # Request and Store Nickname
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        # Print and Broadcast nickname
        print("Nickname is: {}".format(nickname))    
        broadcast("{} joined!".format(nickname).encode('ascii'))  
        client.send('Connection to the server!'.encode('ascii'))

        # Start Handling Thread for client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()