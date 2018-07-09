sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.listen(1)
clientSock, addr = self.sock.accept()
data = cSock.recv(4)
fileLen = struct.unpack('i', data)[0]
 
outfile = open('outputfile.txt', 'w')
while fileLen > 0 :
	readLen = 1024
	if fileLen < readLen: readLen = fileLen
	data = clientSock.recv(readLen)
	outfile.write(data)
	<span style="color:#ff0000;">fileLen -= readLen</span>
outfile.close()