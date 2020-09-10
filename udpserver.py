import socket
import math
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(('127.0.0.1',2152))
while True:
	data,addr=sock.recvfrom(4096)
	print(int(data))
	num=int(data)**0.5
	message=bytes("hey sqrt is r"+str(num),encoding='utf-8')
	sock.sendto(message,addr)
