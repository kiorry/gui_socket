import socket,struct
HOST = ''
PORT =27001
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST,PORT))
sock.listen(1)

clientSock, addr = sock.accept()
data = clientSock.recv(4)
fileLen = struct.unpack('i', data)[0]
 
outfile = open('outputfile.txt', 'w')
while fileLen > 0 :
	readLen = 1024
	if fileLen < readLen: readLen = fileLen
	data = clientSock.recv(readLen)
	outfile.write(data)

outfile.close()