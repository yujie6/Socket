# Socket
Homework of CS391: Computer Network

## 1. Web server
In this project we write a web server serving on localhost. 
Which can respond to `GET` command from clients. 

And we also implement a web client  
```bash
python web-client.py 127.0.0.1 12345 helloworld.html
```

Here is a screenshot 
![Screenshot](./img/2020-10-08-195301_2560x1440_scrot.png)
## 2. Ping server
In this project we write ping server.
And here is the screenshot
![ping server](./img/2020-10-08-203814_2560x1440_scrot.png)
And we also implement UDP-heartbeat.

## 3. SMTP client
In this project, we take advantage of the service from `smtp.qq.com` 
and establish ssl connection to the server to send emails only with python.
Which is fast and convenient. 

On the one hand, we learned several kinds of SMTP messages.
* HELO
* HOLE
* MAIL FROM
* RCPT TO
* DATA
* QUIT
* *AUTH* 

Moreover, to send rich contents such as **images** other than texts in the *DATA* part above, 
we learned [MIME](https://tools.ietf.org/html/rfc2045#section-2.5) 
(Multipurpose Internet Mail Extensions). Especially how to use boundary to 
send multiparty message (text + attachment + html).

Here is the screenshot
![](./img/2020-10-08-201709_2560x1440_scrot.png)
