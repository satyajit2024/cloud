import time
from pymavlink import mavutil

# Set up UDP connection
master = mavutil.mavlink_connection('udpout:localhost:14550')

# Continuously send a heartbeat message
while True:
    # Get heartbeat message
    msg = master.mav.heartbeat_encode(
        mavutil.mavlink.MAV_TYPE_GCS,
        mavutil.mavlink.MAV_AUTOPILOT_INVALID,
        0, 0, 0
    )

    # Print the message
    print("Sending heartbeat message:", msg)
    print("type of message:",type(msg))

    # Send heartbeat
    master.mav.send(msg)

    # Wait for a bit
    time.sleep(1)
