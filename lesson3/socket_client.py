import socket
import time

so = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
)

so.connect(("localhost", 8000))  # Blocking
print("Connected")

time.sleep(5)

sent = so.send("Hello, world!".encode())  # Blocking
print(f"Sent {sent} bytes")

msg = so.recv(1024)  # Blocking
print(f"Message [type: {type(msg)}]: {msg.decode()}")
so.close()
