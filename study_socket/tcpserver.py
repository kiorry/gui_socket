import socket,os,struct
class VoidServer():
    def __init__(self):
        self.HOST = '127.0.0.1'
        self.PORT = 3214
        self.ServerSock = socket.socket()        
        self.ServerSock.bind((self.HOST,self.PORT))
        self.ServerSock.listen(5)
        self.RunListen()
    def RunListen(self):
        client,addr = self.ServerSock.accept()
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
        self.ServerSock.close()

while True:
    try:
        print("server now stand by!")
        server = VoidServer()
    except Exception as e:
        print(e)
        server.ServerSock.close()

# os.system("pause")