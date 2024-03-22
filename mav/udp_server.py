import socket

UDP_IP = '0.0.0.0'  # Listen on all available interfaces
UDP_PORT = 5000     # Choose a port for UDP communication

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((UDP_IP, UDP_PORT))

print(f"UDP server is running on {UDP_IP}:{UDP_PORT}...")

while True:
    data, addr = server_socket.recvfrom(1024)  # Buffer size is 1024 bytes
    print(f"Received message from {addr}: {data.decode()}")
