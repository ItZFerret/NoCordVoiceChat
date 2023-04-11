import socket
import threading

# Server settings
HOST = ''
PORT = 41798

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket to host and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen()

# Clients dictionary
clients = {}

# Send message to all connected clients except sender
def broadcast(sender_socket, message):
    for client_socket in clients:
        if client_socket != sender_socket:
            try:
                client_socket.sendall(message)
            except:
                # Remove the client if it can't be reached
                del clients[client_socket]

# Client handling function
def handle_client(client_socket, address):
    # Receive username from client
    username = client_socket.recv(1024).decode('utf-8')
    print(f"{username} connected from {address}")

    # Add client to dictionary
    clients[client_socket] = username

    # Broadcast that the user has connected
    message = f"{username} has connected\n".encode('utf-8')
    broadcast(client_socket, message)

    # Listen for incoming messages from the client
    while True:
        try:
            # Receive message from client
            message = client_socket.recv(1024)
            if message:
                # Broadcast message to all connected clients
                broadcast(client_socket, message)
            else:
                # Remove the client if the message is empty
                del clients[client_socket]
                message = f"{username} has left the chat\n".encode('utf-8')
                broadcast(client_socket, message)
                break
        except:
            # Remove the client if there is an error
            del clients[client_socket]
            message = f"{username} has left the chat\n".encode('utf-8')
            broadcast(client_socket, message)
            break

    client_socket.close()

# Accept incoming connections
while True:
    client_socket, address = server_socket.accept()

    # Create a new thread for each client
    client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
    client_thread.start()
