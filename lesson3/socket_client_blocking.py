import socket

so = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
)

so.connect(("localhost", 8000))
print("Connected")

msg = input("Enter message: ")

so.sendall(msg.encode())
print("Sent message", msg)

resp = so.recv(1024)
print("Received message", resp)

so.close()
