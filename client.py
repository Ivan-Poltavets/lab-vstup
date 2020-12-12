import socket
import threading
import cesar

def read_sok():
    while 1:
        data = sor.recv(1024)
        decoding = data.decode('utf-8')
        start = decoding.find(']') + 1
        if encrypt.lower() == 'yes':
            print(decoding[:start] + cesar.func(decoding[start:],-1))
        else:
            print(decoding)



server = 'localhost', 9090
alias = input("NAME : ")
encrypt = input('Decrypt message:')
sor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sor.bind(('', 0))
potok = threading.Thread(target=read_sok)
potok.start()
while 1:
    message = cesar.func(input(),1)
    sor.sendto(('[' + alias + ']:' + message).encode('utf-8'), server)

