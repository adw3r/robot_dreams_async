import socket


so = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
)
so.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
so.setblocking(False)
print("Is blocking:", so.getblocking())

so.bind(("localhost", 8000))
so.listen()
print("Listening on localhost:8000")


while True:
    try:
        conn, addr = so.accept()
        print("is blocking:", conn.getblocking())
        print(f"Connection from {addr}")
    except BlockingIOError:
        conn = None
        continue

    while True:
        try:
            msg = conn.recv(1024)
        except BlockingIOError:
            continue
        print("Received", msg.decode())
        break

    conn.sendall(msg)
    print("Sent echo", msg.decode())

    conn.close()
    print("Connection closed")

so.close()
