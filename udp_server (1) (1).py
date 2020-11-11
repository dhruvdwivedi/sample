import socket
import random

SERVER_ADDRESS = '127.0.0.1'
PORT = 2152
BUFFER_SIZE_BYTES = 4096

server_store = {}

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((SERVER_ADDRESS,PORT))


while True:
    data, client_address = server_socket.recvfrom(BUFFER_SIZE_BYTES)
    decoded_data = data.decode('utf-8')
    client_id = decoded_data.split(',')[0]
    number = decoded_data.split(',')[1]
    print("CLient-ID: " + client_id + " Result: " + number)

    result = str(int(number)**0.5)
    
    if client_id in server_store:
        server_id = server_store[client_id]
    else:
        server_id = str(random.randint(1,256))
        server_store[client_id] = server_id

    msg = server_id + "," + result
    server_socket.sendto(msg.encode('utf-8'),client_address)
