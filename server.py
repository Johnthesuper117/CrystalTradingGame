import socket

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Get local machine name (localhost)
    host = '127.0.0.1'
    port = 12345
    
    # Bind the socket to the address and port
    server_socket.bind((host, port))
    
    # Start listening for incoming connections (max 5)
    server_socket.listen(5)
    
    print("Server is listening on {}:{}".format(host, port))
    
    while True:
        # Establish a connection with a client
        client_socket, addr = server_socket.accept()
        print("Got a connection from {}".format(addr))
        
        # Receive data from the client (1024 bytes max)
        data = client_socket.recv(1024).decode('utf-8')
        print("Received data: {}".format(data))
        
        # Send a response back to the client
        response = "Thank you for connecting"
        client_socket.send(response.encode('utf-8'))
        
        # Close the connection with the client
        client_socket.close()

if __name__ == "__main__":
    start_server()
