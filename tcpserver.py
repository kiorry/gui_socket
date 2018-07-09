import socket
HOST = ''
PORT =27001
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s = socket.socket()
# s.bind((HOST,PORT))
# s.listen(2)
# conn,addr = s.accept()
# print('Connect by ',addr)
# while 1:
#     data = conn.recv(1024)
#     print(data)
#     if not data :break
#     conn.send(data)
# conn.close()

class VoidServer():
    HOST = ''
    PORT =27001
    def __init__(self):
        self.ServerSock = socket.socket()
        # self.RunListen()
    def RunListen(self):
        self.ServerSock.bind((VoidServer.HOST,VoidServer.PORT))
        self.ServerSock.listen(2)
        conn,addr = self.ServerSock.accept()
        while True: 
            data = conn.recv(1024)
            print(data)
            if not data :break
            conn.send(data)
        conn.close()
    def ShutServer(self):
        self.ServerSock.close()
        
server = VoidServer()
server.RunListen()