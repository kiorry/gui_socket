# -*- coding: utf-8 -*-
import os
import struct
import socket

HOST = '127.0.0.1'
PORT = 3214
ClientSock = socket.socket()
ClientSock.connect((HOST,PORT))

FileName = "ifelse.exe"
Path = r"./"
FilePath = os.path.join(Path,FileName)
FilePath = os.path.abspath(FilePath)
# print(dir(FilePath))

RF=open(FilePath,"rb")

# data = RF.read(1024)
# print(data)
# ClientSock.sendall(data)        

while True:
    data = RF.read(1024*100)
    if not data:
        print("Not Data!")        
        break        
    else:
        print(RF.tell())
        ClientSock.sendall(data)

        
RF.close()
ClientSock.close()
# pass
