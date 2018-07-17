# -*- coding: utf-8 -*-
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
# 形参用小写加"_"
"""

class Client_:
    def __init__(self,host='127.0.0.1',port="3214"):
        self.sock = socket.socket()
        self.sock.connect((host, int(port)))

    def UploadFile(self,file_path):
        TupleFileInfo = self.GetFileInfomations(file_path)
        if TupleFileInfo:
            #把文件头发过去
            Info = struct.pack('32sL32s',*TupleFileInfo)
            self.sock.send(Info)
            
            data = self.sock.recv(1024)
            print(data)

            ObjFile_ = open(file_path, "rb")
            BytesFile_ = ObjFile_.read()
            self.sock.sendall(BytesFile_)
            ObjFile_.close()
        else:
            self.sock.send("".encode())
            # recvdata = self.sock.recv(1024)
            # print(recvdata)
            self.sock.close()
    
    def GetFileInfomations(self,file_path):
        if os.path.isfile(file_path):
            BytesFileName = os.path.basename(file_path).encode("utf-8")
            IntFileSize = os.stat(file_path).st_size
            BytesFileMD5 = self.GetFileMD5(file_path).encode("utf-8")
            # print(BytesFileMD5)
            return BytesFileName,IntFileSize,BytesFileMD5
        else:
            return 0
    def GetFileMD5(self,file_path):
        File_ = open(file_path,"rb")
        ObjMD5 = hashlib.md5()
        ObjMD5.update(File_.read())
        File_.close()
        print(ObjMD5.hexdigest())
        return ObjMD5.hexdigest()

filename = "13001.ksp"
C=Client_()
C.UploadFile(filename)
# C.sock.close()