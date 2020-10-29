#!/usr/bin/python3.6

import socket



sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)      # For UDP



udp_host = '172.168.1.10'

udp_port = 2152



print (udp_host)

#print type(sock) ============> 'type' can be used to see type

# of any variable ('sock' here)



sock.bind((udp_host,udp_port))



while True:

    print ("Waiting for client...")

    data,addr = sock.recvfrom(1024)

    print (data)

