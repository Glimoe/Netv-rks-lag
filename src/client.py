import socket
import time

HOST = "127.0.0.1"
PORT = 9000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    client.sendall("Hej server".encode())
    data = client.recv(1024)
    print(f"Svar fra server: {data.decode()}")
    time.sleep(30)
