import socket

class VoidClient():
    def __init__(self):
        self.HOST = '127.0.0.1'
        self.PORT = 3214
        self.ClientSock = socket.socket()
        self.ClientSock.connect((self.HOST,self.PORT))
        # self.RunListen()
    def SendData(self,data):        
        while True:
            self.ClientSock.sendall(data.encode())
            rec_data = self.ClientSock.recv(1024)
            print("服务器返回以下消息:",rec_data.decode())
            data = input("请输入你要发送的消息:>>>")
            if not data or data == "exit":
                break
        self.ClientSock.close()
    def ShutServer(self):
        self.ClientSock.close()

client = VoidClient()
client.SendData("abc")