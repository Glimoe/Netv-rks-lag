import socket
import time

HOST = "127.0.0.1"
PORT = 9000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    print(f"Server lytter på {HOST}:{PORT}")
    conn, addr = server.accept()
    with conn:
        print(f"Forbindelse fra {addr}")
        data = conn.recv(1024)
        print(f"Modtaget: {data.decode()}")
        conn.sendall(data)
        time.sleep(30)
