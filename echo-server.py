#!/usr/bin/env python3

import socket

HOST = "0.0.0.0" 
PORT = 65432

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

conn, addr = s.accept()
with conn:
    print("Connected by", addr)
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print("Received from Client: " , data)
        conn.sendall(data)

s.close()
