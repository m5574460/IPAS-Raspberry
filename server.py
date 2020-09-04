import socket
import grovepi
from grovepi import *
import time
import thread

pir = 8
flag = 0
led = 3

pinMode(pir, "INPUT")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('IP', port))
server.listen(5)

print("waiting connect...")

connect, (host, port) = server.accept()
hostname = connect.getsockname()
peername = connect.getpeername()
print(hostname, peername)

def hello():
	while True:
		global flag
		data = connect.recv(1024)
		flag = data
		print(flag)
		connect.sendall(flag)

thread.start_new_thread(hello, ())
while True:
	if flag == "led":
		digitalWrite(led, 1)
	else:
		digitalWrite(led, 0)
	time.sleep(0.5)
