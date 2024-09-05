import selectors
import socket


sel = selectors.DefaultSelector()
print(type(sel))


def read(conn, _):
    data = conn.recv(1024)
    if not data:
        return

    print("Received data:", data.decode())
    conn.sendall(data + b" from server")
    conn.close()


def accept(so, _):
    conn, addr = so.accept()
    print("Accepted connection from", addr)
    conn.setblocking(False)

    sel.register(conn, selectors.EVENT_READ, read)


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

sel.register(so, selectors.EVENT_READ, accept)

# Event loop
while True:
    events = sel.select()
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)
