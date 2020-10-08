from socket import *
from time import time, ctime
import sys
from functools import wraps
import errno
import os
import numpy
import signal


class TimeoutError(Exception):
    pass


def timeout(seconds=10, error_message=os.strerror(errno.ETIME)):
    def decorator(func):
        def _handle_timeout(signum, frame):
            raise TimeoutError(error_message)

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result

        return wraps(func)(wrapper)

    return decorator


@timeout(1, "Packet loss")
def recvFromServer(clientSocket):
    return clientSocket.recvfrom(1024)


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
    message = "Ping " + str(i + 1) + " " + ctime(startTime)[11:19]
    try:
        clientSocket.sendto(message.encode(), (server_ip, server_port))
        encodedModified, serverAddress = recvFromServer(clientSocket=clientSocket)
        endTime = time()
        modifiedMessage = encodedModified.decode()
        print(modifiedMessage)
        rtt = (endTime - startTime) * 1000
        rtt_array.append(rtt)
        print("RTT: %f ms\n" % rtt)

    except:
        print("PING %i Request timed out\n" % (i + 1))

print("10 packets transmitted, %d received, %f percent packet loss" % (len(rtt_array), len(rtt_array) * 10))
print("rtt min/avg/max = %f/%f/%f" % (numpy.min(rtt_array), numpy.average(rtt_array), numpy.max(rtt_array)))
clientSocket.close()
