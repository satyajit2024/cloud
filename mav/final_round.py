import socket
from pymavlink import mavutil

# Set up TCP server
#server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind to localhost and port 5760 (MAVLink default)
#server_socket.bind(('0.0.0.0', 5760))
#server_socket.listen(1)  # Listen for incoming connections

print('Waiting for connection...')
#client_socket, address = server_socket.accept()  # Accept incoming connection
#print('Connected to:', address)

# Create MAVLink connection
mav_conn = mavutil.mavlink_connection(
    'tcpin:0.0.0.0:5760')  # Connect to the TCP server

while True:
    # Receive MAVLink message from vehicle
    msg = mav_conn.recv_match()
    if msg:
        print('Received:', msg)
        # Process the received message as needed
