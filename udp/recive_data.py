import socket

def receive_udp_data(port):
    # Create a UDP socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the specified port
    udp_socket.bind(("0.0.0.0", port))
    print(f"Listening on UDP port {port}...")

    try:
        # Receive data
        while True:
            data, addr = udp_socket.recvfrom(1024)
            print(f"Received: {data.decode()} from {addr}")
    except Exception as e:
        print(f"Error receiving data: {e}")
    finally:
        udp_socket.close()

if __name__ == "__main__":
    # Define the UDP port to listen on
    udp_port = 5005  # Same port number used in the sender script

    # Receive UDP data
    receive_udp_data(udp_port)
