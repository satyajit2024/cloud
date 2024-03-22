import socket

TCP_IP = '0.0.0.0'  # Listen on all available interfaces
TCP_PORT = 5000     # Choose a port for TCP communication

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((TCP_IP, TCP_PORT))
server_socket.listen(1)

print(f"TCP server is running on {TCP_IP}:{TCP_PORT}...")

conn, addr = server_socket.accept()
print(f"Connected by {addr}")

while True:
    data = conn.recv(1024)  # Buffer size is 1024 bytes
    if not data:
        break
    print(f"Received data: {data.decode()}")

    # Echo back the received data to the client
    conn.send(b"Hello local VM")
    print(f"Echoed back data: {data.decode()}")

conn.close()
