import socket
import random

SERVER_ADDRESS = '127.0.0.1'
PORT = 2152
BUFFER_SIZE_BYTES = 4096

client_id = str(random.randint(1,256))
print("Client-ID: " + client_id)


client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    number = str(input("Enter the number: "))
    msg =  client_id + "," + number
    client_socket.sendto(msg.encode('utf-8'),(SERVER_ADDRESS,PORT))
    data, server_address = client_socket.recvfrom(BUFFER_SIZE_BYTES)
    decoded_data = data.decode('utf-8')
    server_id = decoded_data.split(',')[0]
    result = decoded_data.split(',')[1]
    print("Server-ID: " + server_id + " Result: " + result)