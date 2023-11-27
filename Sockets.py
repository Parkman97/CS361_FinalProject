import socket
# Create a socket object
api_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
api_socket.connect(("127.0.0.1", 12345))