#!/usr/bin/env python3

import socket
import sys


HOST = sys.argv[1]
PORT = int(sys.argv[2])

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    txt=input()
    s.sendall(txt.encode())
    data = s.recv(1024)    
    #print("Received:", repr(data), "\n")
    print(data.decode())
