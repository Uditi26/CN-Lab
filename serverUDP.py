from socket import *
serverNamer='127.0.0.0'
serverPort=12000
serverSocket=socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(serverNamer,serverPort)
while(1):
    sentence,add=serverSocket.recvfrom(2048)
    sentence=sentence.decode("utf-8")
    file=open(sentence,"r")
    con=file.read(2048)
    serverSocket.sendto(bytes(con,"utf-8"),add)
    print("Sent file\n")
    print(sentence)
    file.close()
    serverSocket.close()
    