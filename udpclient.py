import socket
client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

msg="25"
client_socket.sendto(msg.encode("utf-8"),('127.0.0.1',2152))
data,addr=client_socket.recvfrom(2152)
print("server says")
print(str(data))
client_socket.close()

