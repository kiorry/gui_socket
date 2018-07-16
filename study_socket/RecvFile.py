import os
import struct
import socket
import time
import threading
import hashlib

"""
命名规则:
变量名用匈牙利命名法
类名|函数(方法)名用大驼峰法
形参用小驼峰
"""

class Server:
    def __init__(self):
        self.sock = socket.socket()
        self.Listen()

    def Listen(self,host='127.0.0.1',port="3214"):
        self.sock.bind((host, int(port)))
        self.sock.listen(5)

    def GetData(self):
        try:
            client, addr = self.sock.accept()
            print(client)
            while True:
                data = client.recv(1024)
                if data:
                    print(data)
                    client.send(data)
                else:
                    client.send("".encode())
                    client.close()
                    self.sock.close()
                    break
        except Exception as e:
            print("内部错误",e)
            self.sock.close()

    def RunListen(self):
        client,addr = self.sock.accept()
        recv_file = open(r"./FileRecv/abc.exe","wb")
        while client:
            try:
                data = client.recv(1024)
                if not data :                
                    print("Not Data!")                    
                    break
                else:
                    print(data)
                    recv_file.write(data)
                    # client.sendall(data)            
            except Exception as e:
                print(e)
                break
        recv_file.close()
        client.close()
        self.sock.close()

# while True:
#     try:
#         server = Server()
#         print("server now stand by!")
#         server.GetData()
#     except Exception as e:
#         print(e)
#         break

try:
    server = Server()
    print("server now stand by!")
    while True:
        server.GetData()
except Exception as e:
    print(e)
# os.system("pause")