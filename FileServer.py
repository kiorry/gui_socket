import socket,os,struct
from io import BytesIO
import hashlib
import threading

class Server:
    def __init__(self,host="127.0.0.1",port= 3124):
        self.host=host
        self.port= port
        # self.start()
    
    def getdata(self,client):        
        struct_format = '64sL32s'
        FileHead_size=struct.calcsize(struct_format)
        FileHead = client.recv(FileHead_size)
        FileName,FileSize,FileMD5 = struct.unpack(struct_format,FileHead)
        # print (FileName,FileSize,FileMD5)
        File_ = BytesIO()
        while 1:
            data = client.recv(1024)
            if data:
                File_.write(data)
                File_.seek(0)
                Fmd = hashlib.md5()
                Fmd.update(File_.read())
                RecMD5 = Fmd.hexdigest()
                if RecMD5 == FileMD5.decode("utf-8"):    
                    # client.send("same".encode("utf-8"))
                    print("same".encode("utf-8"))
                # else:
                    # client.send("diffrence".encode("utf-8"))
            else:
                break
        print("信息接收完成!")
        client.close()

    #启动服务
    def start(self):        
        while 1:
            ServerSock = socket.socket()
            ServerSock.bind((self.host,self.port))
            ServerSock.listen(1)
            client,addr = ServerSock.accept()
            self.getdata(client)

s = Server(host="127.0.0.1",port= 3124)
ths = [threading.Thread(target=s.start) for i in range(2)]
for i in ths:
    i.start()


