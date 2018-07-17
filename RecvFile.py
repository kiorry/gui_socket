import os
import struct
import socket
import time
import threading
import hashlib
from collections import namedtuple

"""
命名规则:
变量名用匈牙利命名法
类名|函数(方法)名用大驼峰法
形参用小驼峰
"""

class Server:
    def __init__(self,host='127.0.0.1',port="3214"):
        self.sock = socket.socket()
        self.sock.bind((host, int(port)))
        self.sock.listen(5)
    def SaveFile(self,data,userName,fileName):
        Path_ = r"FileRecv/%s"%userName
        if not os.path.isdir(Path_):
            os.mkdir(Path_)
        File_Path = os.path.join(Path_, fileName)
        File_ = open(File_Path,"wb")
        File_.write(data)
        File_.close()

    def GetData(self,client):
        print(client)
        data = client.recv(1024)
        print(data)
        try:
            #接收文件头
            if data:
                client.send("Data Correct!".encode("utf-8"))
                File_Name,*File_Header = struct.unpack('32sL32s',data)
                File_Name = File_Name.decode("utf-8").strip("\x00")
                # print(File_Name)
                # print(File_Header)
                File_Data = client.recv(File_Header[0])
                if File_Data:
                    self.SaveFile(File_Data,"wey",File_Name)
                    print(File_Data[:50])
            else:
                client.send("Could Not Send Empty Data !".encode("utf-8"))
                # pass
        except Exception as e:
            client.send("Send Data Error!".encode("utf-8"))
            print(e)
        finally:
            client.close()

    def run(self):
        print("...服务开始...")
        print(threading.enumerate())
        while True:
            print(threading.activeCount())
            client, addr = self.sock.accept()
            client.settimeout(500)
            thread = threading.Thread(target=self.GetData,args=(client,))
            thread.setDaemon(True)
            thread.start()



server = Server()
server.run()
# print("server now stand by!")


# os.system("pause")