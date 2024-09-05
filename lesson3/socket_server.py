import socket

so = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
)
so.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print("Is blocking:", so.getblocking())

so.bind(("localhost", 8000))
so.listen()
print("Listening on localhost:8000")

conn, addr = so.accept()  # Blocking
print(f"Connection from {addr}")

msg = conn.recv(1024)  # Blocking
print(f"Message [type: {type(msg)}]: {msg.decode()}")

sent = conn.send(f"Echo: {msg.decode()}".encode())  # Blocking
print(f"Sent {sent} bytes")

conn.close()
print("Connection closed")

so.close()
