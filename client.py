import socket
import threading
import getpass  # for hiding password input

HOST = '127.0.0.1'
PORT = 5000

def receive_messages(conn):
    while True:
        try:
            msg = conn.recv(1024).decode()
            if msg:
                print("\n" + msg)
        except:
            print("[-] Connection lost.")
            break

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    # Handle login prompts
    while True:
        response = client.recv(1024).decode()
        if response.lower().startswith("❌"):
            print(response)
            client.close()
            return
        elif "Username:" in response:
            username = input(response)
            client.send(username.encode())
        elif "Password:" in response:
            password = getpass.getpass(response)
            client.send(password.encode())
        else:
            print(response)
            break

    threading.Thread(target=receive_messages, args=(client,), daemon=True).start()

    while True:
        msg = input()
        if msg.lower() == 'exit':
            break
        client.send(msg.encode())

    client.close()

if __name__ == "__main__":
    main()
