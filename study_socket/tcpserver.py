import socket,os,struct
class VoidServer():
    def __init__(self):
        self.HOST = '127.0.0.1'
        self.PORT = 3214
        self.ServerSock = socket.socket()        
        self.ServerSock.bind((self.HOST,self.PORT))
        self.ServerSock.listen(5)
    def RunListen(self):
        client,addr = self.ServerSock.accept()
        while True: 
            data = client.recv(1024)
            print(data.decode())
            client.send(data)
            if not data :                
                print("Not Data!",data.decode())
                client.close()
                break
        client.close()
    def ShutdownServer(self):
        self.ServerSock.close()
        
server = VoidServer()
while True:
    print("server now stand by!")
    server.RunListen()