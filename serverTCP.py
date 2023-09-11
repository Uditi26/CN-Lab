from socket import *
serverName='127.0.0.0'
serverPort=12000
serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind(serverName,serverPort)
serverSocket.listen(1)
while (1):
    print("\nReady to send\n")
    connectionSocket,addr=serverSocket.accept()
    sentence=connectionSocket.recv(1024).decode()
    file=(open,"r")
    l=file.read(1024)
    connectionSocket.send(l.encode())
    print("sent\n")
    file.close()
    connectionSocket.close()
    