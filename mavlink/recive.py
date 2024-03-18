import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 8888
BUFFER_SIZE = 1024

def main():
    # Create UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))

    print("Python UDP server is listening...")

    # Receive message from C program
    data, addr = sock.recvfrom(BUFFER_SIZE)
    print("Received message from C:", data.decode())

if __name__ == "__main__":
    main()
