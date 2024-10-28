import socket  

def start_server():
    # Layer 7: Application Layer
    # This layer interacts with the user by asking for a name and sending/receiving messages
    host = '0.0.0.0'  
    port = 12345  

    # Layer 4: Transport Layer
    # TCP is used for data transfer
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Layer 3: Network Layer
    # Defines the IP address and port where the server will listen
    server_socket.bind((host, port))
    print(f"Server listening on {host}:{port}...")

    # Layer 5: Session Layer
    # Manages the session by creating the connection with the client
    server_socket.listen(1)  
    conn, addr = server_socket.accept() 
    print(f"Connected to {addr}")

    # Layer 6: Presentation Layer
    # Handles data encoding/decoding between bytes and string
    client_name = conn.recv(1024).decode('utf-8')  
    print(f"{client_name} joined the chat!")

    server_name = input("Enter your name: ")

    while True:
        # Layer 2: Data Link Layer
        # Data is sent in frames through the established connection.
        data = conn.recv(1024).decode('utf-8')  
        if not data:
            print(f"{client_name} disconnected.")
            break

        print(f"{client_name}: {data}")

        # Layer 1: Physical Layer
        # The physical hardware transmits the data between devices (Wi-Fi or Ethernet).
        message = input(f"{server_name}: ")
        conn.send(message.encode('utf-8'))  

    conn.close()  

if __name__ == "__main__":
    start_server()