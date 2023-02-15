import socket
import threading

# Choosing Nicknames
nickname = input("Enter your Nickname: ")

# Connecting to server
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',55555))

def receive():
    while True:
        try:
            # Receive Message from Server.
            # If 'NICK' Send Nickname
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        
        except:
            # Close Connection When Error Occurs
            print("An error occured!")
            client.close()
            break

# Sending Message To Server
def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('ascii'))

# Starting Threads for Listening and Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()