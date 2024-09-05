import socket

so = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
)
so.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
so.setblocking(True)

so.bind(("localhost", 8000))
so.listen()
print("Listening on localhost:8000")

conn, addr = so.accept()
print(f"Connection from {addr}")

msg = conn.recv(1024)
print("Received", msg.decode())

conn.sendall(msg)
print("Sent echo", msg.decode())

conn.close()
print("Connection closed")

so.close()
