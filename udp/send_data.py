import socket

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Get the server IP address and port
server_ip = "192.168.1.109"  # Replace with the server's IP address
server_port = 5005

# Define the message to send
message = b"Hello, Server!"

# Send the message to the server
server_address = (server_ip, server_port)
client_socket.sendto(message, server_address)
print(f"Sent {message.decode()} to {server_address}")

# Receive the response from the server
data, server_address = client_socket.recvfrom(1024)
print(f"Received {data.decode()} from {server_address}")
