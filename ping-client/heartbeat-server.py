# UDPPingerServer.py
# We will need the following module to generate randomized lost packets
import random
import time
from socket import *
import select

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000))
last_time = 0.0
last_client = ""
while True:
    # Receive the client packet along with the address it is coming from
    ready = select.select([serverSocket], [], [], 2)
    if ready[0]:
        message, address = serverSocket.recvfrom(1024)
        print("receive from client: ", address, message)
        t = message[-24:]
        send_time = time.mktime(time.strptime(t.decode(), "%a %b %d %H:%M:%S %Y"))
        last_time = send_time
        last_client = address
        message = message.upper()
        serverSocket.sendto(message, address)
        print("send complete")
        cur_time = time.time()
        # Capitalize the message from the client
    else:
        if last_client != "":
            print("client is dying!", last_client)
