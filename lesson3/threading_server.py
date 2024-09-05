import socket
import threading
from cpu_tasks import do_calc


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


def handle_connection(conn):
    while True:
        try:
            msg = conn.recv(1024)
        except BlockingIOError:
            continue
        print("Received", msg.decode())
        break

    resp = f"Echo: {msg.decode()} {do_calc()}"
    conn.sendall(resp.encode())
    print("Sent echo", msg.decode())

    conn.close()
    print("Connection closed")


threads = []

try:
    while True:
        try:
            conn, addr = so.accept()
            print("is blocking:", conn.getblocking())
            print(f"Connection from {addr}")
        except BlockingIOError:
            conn = None
            continue
        else:
            t = threading.Thread(
                target=handle_connection,
                args=(conn,),
                daemon=True,
            )
            t.start()
            threads.append(t)
except KeyboardInterrupt:
    for t in threads:
        t.join()


so.close()
