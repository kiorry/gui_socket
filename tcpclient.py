import socket

host = "127.0.0.1"
port = 12345

s = socket.socket()

s.connect((host,port))

cli_data = "你好!"

s.sendall(cli_data.encode())



while 1:
    ser_data = s.recv(1024)
    print("从服务器收到的信息是:",ser_data.decode())

    data = input(">>>")
    if not data:
        break
    if data == "exit":
        s.close()
    else:
        s.sendall(data.encode())

    
s.close()