# CS-216_P2P_Hashpa
# Peer-to-Peer Chat Application

## Team Information

- *Team Name:* Hashpa
- *Team Members:*
  - Lawadya Yashwanth Chowhan - 230001046
  - Machana Mohan Prudhvi Sai - 230001047
  - Mallisetti Rishik Preetham - 230001048

---

## Project Description

This project is a *Peer-to-Peer (P2P) Chat Application* implemented using Python. The chat system allows users to communicate directly without a central server. The key functionalities include:

- Simultaneous message sending and receiving.
- Communication with multiple peers.
- Querying and retrieving a list of active peers.
- Connecting to discovered peers.
- Managing inactive peers by removing them automatically.

---

## Features

*Simultaneous Send & Receive* - The receive function runs in a separate thread.

*Peer Discovery* - Maintains a list of peers who have communicated directly.

*Standardized Message Format* - <IP:PORT> <TEAM_NAME> <MESSAGE>

 *Connection Management* - Allows connecting to active peers and removing inactive ones.

*Safe Multi-threading* - Uses thread locks to avoid conflicts when updating the peer list.

*Fixed Port Support* - Ensures consistency when receiving messages from the same peer.

---

## Installation & Running Instructions

### Prerequisites

- Python 3.x installed

### Steps to Run

1. Clone this repository:

   bash
   git clone https://github.com/yourusername/your_repository_name.git
   cd your_repository_name
   

2. Run the script:

   bash
   python3 p2p_network.py
   

3. Enter your port number when prompted.

4. Use the menu options to send messages, query peers, or manage connections.

---

## Example Workflow

### *Scenario: Chatting Between Two Peers*

1. *Open multiple terminals* and run the script on different ports.
2. *Start Peer 1* on port 8080:
   
   Enter the port number for your peer: 8080
   
3. *Start Peer 2* on port 9090:
   
   Enter the port number for your peer: 9090
   
4. *Peer 1 sends a message to Peer 2:*
   
   Enter recipient's IP: 127.0.0.1
   Enter recipient's Port: 9090
   Enter message: Hello, Peer 2!
   
5. *Peer 2 receives the message:*
   
   📩 Message from 127.0.0.1:8080 (Hashpa) → Hello, Peer 2!
   
6. *Query connected peers:*
   
   Active Peers:
   Hashpa → 127.0.0.1:8080
   

---

## Bonus Implementation

*Connect to Discovered Peers* - The connect() function allows automatic connection with peers.



---

## Technologies Used

- *Python* (Sockets, Threading)

---

## Notes

- Ensure that your firewall allows communication over the chosen ports.
- Run the script on multiple terminals or machines to establish a real P2P chat network.
