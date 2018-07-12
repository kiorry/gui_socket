# -*- coding: utf-8 -*-
import os
import struct
import socket
import time
import threading
import hashlib

def GetFileMD5(file_path):
    ReadFile = open(file_path,"rb")
    Fmd = hashlib.md5()
    Fmd.update(ReadFile.read())
    ReadFile.close()
    return Fmd.hexdigest()

def SendFile(my_client,file_path):
    """
    1.传入一个文件路径,把该文件的文件名,文件大小,MD5码发送到服务端.
    2.把该文件发送到服务端.
    """
    if os.path.isfile(file_path):
        FileName = os.path.basename(file_path)
        FileSize = os.stat(file_path).st_size
        FileMD5 = GetFileMD5(file_path)
        FileHead = struct.pack('64sl64s',FileName.encode("utf-8"),FileSize,FileMD5.encode("utf-8"))
        my_client.send(FileHead)
        
    __File = open(file_path,"rb")
    while True:
        data = __File.read(1024)
        if data:
            my_client.send(data)
        else:
            print("Not Data!")        
            break
    __File.close()
    my_client.close()


# threads = [threading.Thread(target=SendFile,args=(file_path,)) for i in range(4)]
# for i in threads:
#     i.start()

t1 = time.time()

HOST = '127.0.0.1'
PORT = 3214
ClientSock = socket.socket()
ClientSock.connect((HOST,PORT))
filename = "ifelse.exe"
SendFile(ClientSock,filename)

print(time.time()-t1) 
