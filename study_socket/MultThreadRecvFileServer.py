# __auth__ =  "嘻嘻TV²º¹⁷"

import socket,time,traceback
import threading

def data_processor(client,address):
    try:
        print(address)
        client.settimeout(500)
        rec_data = client.recv(20400000000)

        with open("FileRecv/{}.txt".format(int(time.time())),"wb") as f:
            f.write(rec_data)

    except socket.timeout:
        traceback.print_exc()
        print( 'time out')

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('127.0.0.1', 3214))
    sock.listen(1)
    while True:
        print("go.................")
        client,address = sock.accept()
        thread = threading.Thread(target=data_processor, args=(client,address))
        thread.start()

if __name__ == '__main__':
    main()
