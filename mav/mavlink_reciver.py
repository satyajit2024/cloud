import socket
from pymavlink import mavutil

mav_conn = mavutil.mavlink_connection(
    'tcp:0.tcp.in.ngrok.io:17531')  # Connect to the TCP server


while True:
    # Receive MAVLink message from vehicle
    msg = mav_conn.recv_match()
    if msg:
        print('Received:', msg)
        # Process the received message as needed
