import socket
import threading
import socket
import threading

# Dictionary to store known peers { (IP, Port): "Peer Name" }
peer_list = {}
connected_peers = set()
lock = threading.Lock()
TEAM_NAME = "Hashpa"

# Function to receive messages and track peers
def receive_messages(server_socket):
    while True:
        try:
            client, addr = server_socket.accept()
            message = client.recv(1024).decode()
            try:
                sender_info, team_name, actual_message = message.split(" ", 2)
                sender_ip, sender_port = sender_info.split(":")
                sender_port = int(sender_port)

                if actual_message == "PING":
                    client.close()
                    continue

                with lock:
                    if (sender_ip, sender_port) not in peer_list:
                        peer_list[(sender_ip, sender_port)] = team_name

                print(f"\n 📩 Message from {sender_ip}:{sender_port} ({team_name}) → {actual_message}")
                
            except Exception as e:
                print(f"\n Received malformed message: {message}")

            client.close()
        except Exception as e:
            print(f"\n[Error in Receiving] {e}")

# Function to send messages with the given format
def send_messages(my_ip, my_port):
    while True:
        try:
            choice = input("\n1. Send Message\n2. Query Active Peers\n3. Connect to Peers\n4. Remove Inactive Peers \n0. Quit\nEnter choice: ").strip()

            if choice == "1":
                target_ip = input("Enter recipient's IP address: ").strip()
                target_port = input("Enter recipient's port number: ").strip()

                if not target_port.isdigit():
                    print("Invalid port! Please enter a number.")
                    continue

                target_port = int(target_port)
                message = input("Enter your message: ").strip()
                formatted_message = f"{my_ip}:{my_port} {TEAM_NAME} {message}"

                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    client.connect((target_ip, target_port))
                    client.send(formatted_message.encode())
                    print("Message sent!")
                except Exception as e:
                    print(f"Connection failed: {e}")
                finally:
                    client.close()

            elif choice == "2":
                with lock:
                    print("\n Active Peers:")
                    if peer_list:
                        for (ip, port), name in peer_list.items():
                            connection_status = " (Connected)" if (ip, port) in connected_peers else ""
                            print(f" {name} → {ip}:{port}{connection_status}")
                    else:
                        print("No active peers yet.")

            elif choice == "3":
                print("\n Connecting to known peers...")
                with lock:
                    for (ip, port) in list(peer_list.keys()):
                        if (ip, port) not in connected_peers:
                            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            try:
                                client.connect((ip, port))
                                client.send(f"{my_ip}:{my_port} {TEAM_NAME} Hello, I am connecting!".encode())
                                connected_peers.add((ip, port))
                                print(f"Connected to {ip}:{port}")
                            except Exception as e:
                                print(f"Failed to connect to {ip}:{port}: {e}")
                            finally:
                                client.close()

            elif choice == "4":
                print("\nChecking for inactive peers...")
                remove_inactive_peers()
                    
            elif choice == "0":
                print("Exiting chat. Goodbye!")
                break

            else:
                print("Invalid choice! Please enter 1, 2, 3, 4, or 0.")

        except Exception as e:
            print(f"\n[Error in Sending] {e}")

# Function to check and remove inactive peers
def remove_inactive_peers():
    to_remove = []
    with lock:
        for (ip, port) in list(peer_list.keys()):
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(2)
            try:
                client.connect((ip, port))
                client.send(f"{ip}:{port} {TEAM_NAME} PING".encode())
                client.close()
            except:
                to_remove.append((ip, port))
                
        for peer in to_remove:
            peer_list.pop(peer, None)
            print(f"Removed inactive peer: {peer[0]}:{peer[1]}")

# Main function
def main():
    my_ip = socket.gethostbyname(socket.gethostname())  
    my_port = input("Enter the port number for your peer: ").strip()

    if not my_port.isdigit():
        print("Invalid port! Please enter a number.")
        return

    my_port = int(my_port)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((my_ip, my_port))
    server_socket.listen(5)
    print(f"Server listening on {my_ip}:{my_port}")

    receive_thread = threading.Thread(target=receive_messages, args=(server_socket,))
    receive_thread.daemon = True
    receive_thread.start()

    send_messages(my_ip, my_port)

if __name__ == "__main__":
    main()