import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(('localhost',9090))
client = []
print ('Start Server')
while 1:
        data , addres = sock.recvfrom(1024)

        print ("["+addres[0]+"]=[" + str(addres[1])+"]")
        if  addres not in client:
                client.append(addres)
        for clients in client:
                if clients == addres :
                     continue
                sock.sendto(data,clients)


