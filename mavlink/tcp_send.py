from pymavlink import mavutil
import time

# TCP connection settings
tcp_ip = '192.168.0.109'  # IP address of the receiver
tcp_port = 5760  # TCP port to connect to (default for MAVLink)

# Create a MAVLink TCP connection
mav_connection = mavutil.mavlink_connection(f'tcp:{tcp_ip}:{tcp_port}')

# Send heartbeat messages every second
while True:
    mav_connection.mav.heartbeat_send(mavutil.mavlink.MAV_TYPE_GCS,
                                      mavutil.mavlink.MAV_AUTOPILOT_INVALID,
                                      0,
                                      0,
                                      0)
    time.sleep(1)
