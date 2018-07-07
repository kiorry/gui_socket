import socket
print("程序启动")
host = ""
port = 12345

s = socket.socket()

s.bind((host,port))
s.listen(5)
client,address = s.accept()

client.sendall("您的客户端地址:".encode())
# client.sendall(address)
client.sendall("系统接入成功,请输入指令".encode()) 
while True:
    data = client.recv(1024)
    if data != "":        
        if data == "exit".encode():
            s.close()
        else:            
            print(data.decode())
    
print("程序结束")