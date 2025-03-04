import socket

def start_client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Get local machine name (localhost)
    host = '127.0.0.1'
    port = 12345
    
    # Connect to the server
    client_socket.connect((host, port))
    
    # Send data to the server
    message = "Hello, Server!"
    client_socket.send(message.encode('utf-8'))
    
    # Receive response from the server
    response = client_socket.recv(1024).decode('utf-8')
    print("Received response from server: {}".format(response))
    
    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    start_client()
