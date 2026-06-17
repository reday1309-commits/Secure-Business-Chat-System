# Secure Multi-Client Chat System

## 📌 Description
A secure real-time multi-client chat system built using Python sockets, threading, and bcrypt-based authentication. The system allows multiple users to connect, authenticate securely, and communicate in real time.

---

## 🚀 Features
- Multi-client support using threading
- Secure user authentication using bcrypt
- Real-time message broadcasting
- Login system (username & password)
- Exit command support
- Server-side user management

---

## 🛠️ Technologies Used
- Python
- Socket Programming
- Threading
- bcrypt (Password hashing)
- getpass (Secure password input)

---

## ⚙️ How It Works
1. Server starts and admin creates allowed users with passwords.
2. Passwords are hashed using bcrypt for security.
3. Clients connect to server via IP and port.
4. Users must login with valid credentials.
5. After authentication, messages are broadcast to all connected clients in real time.

---

## ▶️ How to Run

### 1. Install dependencies
```bash
pip install bcrypt
