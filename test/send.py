import time
from pymavlink import mavutil

# Sender's IP address and port
sender_ip = '20.244.105.241'
sender_port = 14550  # MAVLink default UDP port

# Create a UDP socket for sending MAVLink messages
sender_socket = mavutil.mavlink_connection(f'udp:{sender_ip}:{sender_port}')

# Example: Send a heartbeat message every 1 second
while True:
    sender_socket.mav.heartbeat_send(
        mavutil.mavlink.MAV_TYPE_GCS, mavutil.mavlink.MAV_AUTOPILOT_INVALID, 0, 0, 0)
    time.sleep(1)
