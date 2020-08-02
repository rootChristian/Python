#CLIENT WEB
#!/usr/bin/env python
#coding:utf-8

import socket

host, port=('localhost', 8888)

socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #definire la socket en ipv4 et tcp

try:
    socket.connect((host, port))
    print("Client connected...")

    data="hello, i'm client! ->"
    data=data.encode("utf-8")
    socket.sendall(data)
except ConnectionRefusedError:
    print("Connection fail!!!")
finally:
    socket.close()
    
