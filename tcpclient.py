from socket import socket, AF_INET, SOCK_STREAM
import select

if __name__ == '__main__':
    serverName = 'localhost'
    serverPort = 2
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    sentence = raw_input('Input sentence: ')
    clientSocket.send(sentence)
    modifiedSentence = clientSocket.recv(1024)
    print ('From Server: ' +  modifiedSentence)
    clientSocket.close()