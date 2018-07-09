import socket

class VoidClient():
    HOST = ''
    PORT =27001
    def __init__(self):
        self.ClientSock = socket.socket()
        # self.RunListen()
    def SendData(self,data):
        self.ClientSock.send(data.encode())
        data = self.ClientSock.recv(1024)
        print(data.decode())
    def ShutServer(self):
        self.ClientSock.close()

client = VoidClient()
client.SendData("abc")