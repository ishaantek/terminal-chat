import socket 

def start_client():
    # Layer 7: Application Layer
    # Interacts with the user by asking for a name and sending/receiving messages
    host = input("Enter server IP: ")
    port = 12345 

    # Layer 4: Transport Layer
    # Establish a TCP connection for data transfer
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Layer 3: Network Layer
    # Use the IP address and port to connect to the server
    client_socket.connect((host, port))
    print("Connected to the server.")

    # Layer 6: Presentation Layer
    # Encode the client's name and send it to the server
    client_name = input("Enter your name: ")
    client_socket.send(client_name.encode('utf-8'))  

    while True:
        # Layer 1: Physical Layer
        # The physical hardware sends and receives the messages 
        message = input(f"{client_name}: ")  
        client_socket.send(message.encode('utf-8'))  

        # Layer 2: Data Link Layer
        # Data is transmitted as frames over the network
        data = client_socket.recv(1024).decode('utf-8') 
        if not data:
            print("Server disconnected.")
            break

        print(f"Server: {data}")

    client_socket.close() 

if __name__ == "__main__":
    start_client()
