from socket import *
import sys

if len(sys.argv) != 4:
    print("Wrong number of arguments.")
    print("Usage: web-client.py <server_host> <server_port> <filename>")
    sys.exit()

# Preparing the socket
serverHost, serverPort, filename = sys.argv[1:]
clientSocket = socket(AF_INET, SOCK_STREAM)
try:
    clientSocket.connect((serverHost, int(serverPort)))
except:  # In case the server is not available
    print("Server not found")
    clientSocket.close()
    sys.exit()

print("Connect done!")

httpRequest = "GET /" + filename + " HTTP/1.1\r\n\r\n"
clientSocket.send(httpRequest.encode())
print("Request message sent.")
data = ""
while True:
    clientSocket.settimeout(5)
    newData = clientSocket.recv(1024).decode()
    data += newData
    if len(newData) == 0:
        break
print(data)
# Closing socket and ending the program
clientSocket.close()
