import socket
import threading
import bcrypt
import getpass 

HOST = '127.0.0.1'   
PORT = 5000
clients = {}  # conn: username
users = {}    # username: password (you input this at server start)


def setup_users():
    print("Setup Authorized Users")
    count = int(input("How many users do you want to allow? "))
    for _ in range(count):
        username = input("Username: ").strip()
        # Use getpass.getpass to hide password input in terminal
        password = getpass.getpass(f"Password for {username}: ").strip()

        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        users[username] = hashed
    print("User setup complete.\n")

def broadcast(message, sender_conn):
    for client_conn in clients:
        if client_conn != sender_conn:
            try:
                client_conn.send(message.encode())
            except:
                pass

def handle_client(conn, addr):
    conn.send("Username: ".encode())
    username = conn.recv(1024).decode().strip()

    conn.send("Password: ".encode())
    password = conn.recv(1024).decode().strip()

    if username not in users or not bcrypt.checkpw(password.encode(), users[username]):
     conn.send(" Authentication failed. Connection closing.".encode())
     conn.close()
     return


    clients[conn] = username
    conn.send(f" Welcome, {username}!\nType 'exit' to leave.\n".encode())
    print(f"[+] {username} ({addr}) connected.")
    broadcast(f" {username} has joined the chat!", conn)

    while True:
        try:
            message = conn.recv(1024).decode()
            if not message or message.lower() == 'exit':
                break
            broadcast(f"{username}: {message}", conn)
        except:
            break

    print(f"[-] {username} disconnected.")
    broadcast(f"{username} has left the chat.", conn)
    del clients[conn]
    conn.close()

def main():
    setup_users()
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"Server listening on {HOST}:{PORT}\n")

    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()

if __name__ == "__main__":
    main()