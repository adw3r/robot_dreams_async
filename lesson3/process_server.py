import socket
import multiprocessing as mp
import time
import random


def handle_connection(conn):
    while True:
        try:
            msg = conn.recv(1024)
        except BlockingIOError:
            continue
        print("Received", msg.decode())
        break

    t = random.randint(1, 5)
    time.sleep(t)
    resp = f"Echo: {msg.decode()} - {t}"
    conn.sendall(resp.encode())
    print("Sent echo", msg.decode())

    conn.close()
    print("Connection closed")


def main():
    so = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
    )
    so.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    so.setblocking(True)
    print("Is blocking:", so.getblocking())

    so.bind(("localhost", 8000))
    so.listen()
    print("Listening on localhost:8000")

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
                t = mp.Process(
                    target=handle_connection,
                    args=(conn,),
                    daemon=True,
                )
                t.start()
                threads.append(t)
    except KeyboardInterrupt:
        for t in threads:
            t.kill()
            t.join()

    so.close()


if __name__ == "__main__":
    main()
