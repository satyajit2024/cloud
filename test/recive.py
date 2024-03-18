from pymavlink import mavutil

# Set up UDP connection
master = mavutil.mavlink_connection('udpin:localhost:14550')

# Continuously receive messages
while True:
    try:
        # Wait for a message
        msg = master.recv_match()

        # Print message type and contents
        if msg is not None:
            print("Received:", msg.get_type(), msg)
            print("Type of message :",type(msg))
    except KeyboardInterrupt:
        break
