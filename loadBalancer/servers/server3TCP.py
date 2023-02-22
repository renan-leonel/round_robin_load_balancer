import socket
from _thread import *

host = '127.0.0.3'
port = 1233
ThreadCount = 0

def client_handler(connection):
    data = connection.recv(2048)
    message = data.decode('utf-8')
    print(f' {message}')

def accept_connections(ServerSocket):
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]), end='')
    start_new_thread(client_handler, (Client, ))

def start_server(host, port):
    ServerSocket = socket.socket()
    try:
        ServerSocket.bind((host, port))
    except socket.error as e:
        print(str(e))
    print(f'Server is listing on the port {port}...')
    ServerSocket.listen()

    while True:
        accept_connections(ServerSocket)

start_server(host, port)