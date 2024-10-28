# Terminal Chat Application using Python

This is a simple **terminal-based chat application** that allows two devices (e.g., two computers on the same network) to chat using Python's socket library. Each user can **choose their name**, and messages are tagged with the sender’s name.

## How It Works

- One device acts as the **server** and listens for incoming connections.
- The other device acts as the **client** and connects to the server using the **server’s IP address** and port.
- Both users can enter their **names**, and all messages are displayed with proper name tags.

---

## Setup Instructions

### 1. Prerequisites

- **Python 3** installed on both devices.
- Both devices connected to the **same Wi-Fi network** or on the **same LAN**.

---

### 2. Running the Server (Device 1)

1. Open **terminal** (on macOS/Linux) or **Command Prompt** (on Windows).
2. Navigate to the folder where `server.py` is located.
3. Run the following command:

   ```bash
   python3 server.py  # For macOS/Linux
   python server.py   # For Windows
4. The server will display the IP address it is listening on (or use `ifconfig`/`ipconfig` to find the IP manually).

---

### 3. Running the Client (Device 2)

1. Open **terminal** (on macOS/Linux) or **Command Prompt** (on Windows).
2. Navigate to the folder where `client.py` is located.
3. Run the following command:
   ```bash
   python3 client.py # For macOS/Linux
   python client.py # For Windows
4. When prompted, **enter the server’s IP address** (from Step 2).
5. Enter your **name**, and the chat session will start.