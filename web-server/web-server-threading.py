# import socket module
from socket import *
import threading
import os.path


def handle_client(connectionSocket):
    try:
        message = connectionSocket.recv(2048)  # Fill in start #Fill in end
        print("Get message: ", message.decode())
        filename = message.split()[1]
        # print("Try to find file: ", filename.decode())
        output_data = open(filename[1:]).read()
        # Send one HTTP header line into socket
        header = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n"
        # Fill in start #Fill in end
        # Send the content of the requested file to the client

        connectionSocket.send(header.encode('utf-8'))
        connectionSocket.send("\r\n".encode())
        for i in range(0, len(output_data)):
            connectionSocket.send(output_data[i].encode('utf-8'))
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        print("File does not exists!")
        connectionSocket.send("HTTP/1.1 404 Not Found\r\ncontent-type:text/html\r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send('''
            <html>
                <head>
                <title>404 Not Found</title>
                <p>404 Not Found!</p>
                </head>
            </html>
            '''.encode())
        connectionSocket.close()


serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket
# Fill in start
serverSocket.bind(('localhost', 12345))
serverSocket.listen(1)
# Fill in end
while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    client_handler = threading.Thread(target=handle_client, args=(connectionSocket,))
    client_handler.start()
    # print(connectionSocket, addr)

    # Send response message for file not found
    # Close client socket
# Fill in start
serverSocket.close()
# Fill in end
