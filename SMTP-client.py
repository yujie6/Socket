from socket import *
import time
import ssl
import base64
import email.mime.multipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailServer_sjtu = ("smtp.sjtu.edu.cn", 587)  # Fill in start #Fill in end
mailServer_qq = ('smtp.qq.com', 465)
user_name = b'eXVqaWUxMjRAcXEuY29t\r\n'
pass_word = b'\r\n'
imgae_address = "/home/yujie6/Pictures/PCR/uni.jpg"
# Create socket called clientSocket and establish a TCP connection with mailserver
# Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket = ssl.wrap_socket(clientSocket, cert_reqs=ssl.CERT_NONE, ssl_version=ssl.PROTOCOL_SSLv23)
clientSocket.connect(mailServer_qq)
# Fill in end
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')
# Send HELO command and print server response.
heloCommand = 'EHLO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print("After HELO command: " + recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

login = 'AUTH LOGIN\r\n'
clientSocket.send(login.encode())
recv_login = clientSocket.recv(1024).decode()
print("After LOGIN: " + recv_login)

login_hint = base64.b64decode(recv_login[4:])
print(login_hint)

clientSocket.send(user_name)
recv_user_name = clientSocket.recv(1024).decode()
print("After USERNAME: " + recv_user_name)
login_hint1 = base64.b64decode(recv_user_name[4:])
print(login_hint1)

clientSocket.send(pass_word)
recv_pass_word = clientSocket.recv(1024).decode()
print("After PASSWORD: " + recv_pass_word)
# Send MAIL FROM command and print server response.
# Fill in start
mailFrom = 'MAIL FROM:<784727124@qq.com>\r\n'
clientSocket.send(mailFrom.encode())
recv2 = clientSocket.recv(1024).decode()
print("After MAIL FROM command: " + recv2)

# TEST
# help = 'HELP\r\n'
# clientSocket.send(help.encode())
# recv_help = clientSocket.recv(1024).decode()
# print("After HELP: " + recv_help)
#

# Fill in end
# Send RCPT TO command and print server response.
# Fill in start
rcptTo = 'RCPT TO:<yujie6@sjtu.edu.cn>\r\n'
clientSocket.send(rcptTo.encode())
recv3 = clientSocket.recv(1024).decode()
print("After RCPT TO command: " + recv3)
# Fill in end
# Send DATA command and print server response.
# Fill in start
data = "DATA\r\n"
clientSocket.send(data.encode())
recv4 = clientSocket.recv(1024).decode()
print("After DATA command: " + recv4)
# Fill in end
# Send message data.
# Fill in start
subject = "Subject: From python\r\n"
clientSocket.send(subject.encode())
clientSocket.send(b'X-Mailer:yujie\'s mailer\r\n')  # mailer
# clientSocket.send(b'Content-Transfer-Encoding:7bit\r\n')
msg = email.mime.multipart.MIMEMultipart()
msg.attach(MIMEText('<html><body><h1>Hello</h1><p><img src="cid:uni"></p></body></html>', 'html', 'utf-8'))
with open(imgae_address, 'rb') as f:
    mime_img = MIMEBase('image', 'png', filename='uni.jpg')
    mime_img.add_header('Content-Disposition', 'attachment', filename='uni.jpg')
    mime_img.add_header('Content-ID', '<uni>')
    mime_img.set_payload(f.read())
    encoders.encode_base64(mime_img)
    msg.attach(mime_img)


clientSocket.send(msg.__bytes__())
clientSocket.send(endmsg.encode())

# Fill in end
# Message ends with a single period.
# Fill in start
recv_msg = clientSocket.recv(1024)
print("After sending message body: " + recv_msg.decode())
# Fill in end
# Send QUIT command and get server response.
# Fill in start
quit = "QUIT\r\n"
clientSocket.send(quit.encode())
recv5 = clientSocket.recv(1024)
print(recv5.decode())
clientSocket.close()
# Fill in end
