import os

mode = input("Enter 'listen' or 'connect': ").strip()

if mode == 'listen':
    print("Listening for incoming messages...")
    os.system("nc -l 12345 | tee received.txt")
elif mode == 'connect':
    ip = input("Enter IP of listener: ").strip()
    print(f"Connecting to {ip}...")
    os.system(f"nc {ip} 12345 | tee received.txt")
