    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((serverIp, serverPort))
    inputfiledata = open('input.txt').read()
    inputfiledataLen = len(inputfiledata)
    data = struct.pack('i', inputfiledataLen)
    sock.send(data)
    while inputfiledataLen > 0:
    	readLen = 1024
    	if inputfiledataLen < readLen: readLen = inputfiledataLen
    	sock.send(inputfiledata[:readLen])
    	inputfiledataLen -= readLen
    	inputfiledata = inputfiledata[readLen:]
    sock.close()