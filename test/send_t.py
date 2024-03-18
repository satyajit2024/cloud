import socket

SERVER_IP = '192.168.0.109'  # Replace with the server's IP address
SERVER_PORT = 12345  # Replace with the server's port number

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, SERVER_PORT))

# Receive server information
server_info = client_socket.recv(1024).decode('utf-8')
print(f"Server information received: {server_info}")

# Send data to the server
message = "Hello, server!"
client_socket.send(message.encode('utf-8'))

client_socket.close()

