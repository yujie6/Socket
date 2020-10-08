# UDPPingerServer.py
# We will need the following module to generate randomized lost packets
import random
import time
from socket import *
import signal
import errno
import os
from functools import wraps


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


@timeout(1, "Timeout!")
def recvFromClient(serverSocket):
    return serverSocket.recvfrom(1024)


# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000))
last_time = 0.0
last_client = ""
while True:
    # Receive the client packet along with the address it is coming from
    try:
        message, address = recvFromClient(serverSocket)
        print("receive from client: ", address, message)
        t = message[7:]
        send_time = time.mktime(time.strptime(t, "%a %b %d %H:%M:%S %Y"))
        last_time = send_time
        last_client = address
        message = message.upper()
        serverSocket.sendto(message, address)
        print("send complete")
        cur_time = time.time()
        # Capitalize the message from the client

    except:
        if last_client != "":
            print("Client is dying")
            print(last_client)
