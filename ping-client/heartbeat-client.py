from socket import *
from time import time, ctime
import sys
import signal
import errno
import os
from functools import wraps
import numpy


server_ip = ""
server_port = 0
if len(sys.argv) == 3:
    server_ip = sys.argv[1]
    server_port = sys.argv[2]
else:
    server_ip = "127.0.0.1"
    server_port = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)
rtt_array = []
for i in range(10):
    startTime = time()  # Retrieve the current time
    message = "Ping " + str(i + 1) + " " + ctime(startTime)

    clientSocket.sendto(message.encode(), (server_ip, server_port))
    encodedModified, serverAddress = clientSocket.recvfrom(1024)
    endTime = time()
    modifiedMessage = encodedModified.decode()
    print(modifiedMessage)
    rtt = (endTime - startTime) * 1000
    rtt_array.append(rtt)
    print("RTT: %f ms\n" % rtt)

print("10 packets transmitted, %d received, %f percent packet loss" % (len(rtt_array), len(rtt_array) * 10))
print("rtt min/avg/max = %f/%f/%f" % (numpy.min(rtt_array), numpy.average(rtt_array), numpy.max(rtt_array)))
clientSocket.close()
