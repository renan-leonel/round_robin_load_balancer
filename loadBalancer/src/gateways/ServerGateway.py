import socket
PORT_TCP1 = 1231
PORT_TCP2 = 1232
PORT_TCP3 = 1233
PORT_UDP2 = 1234
PORT_UDP3 = 1235


class ServerGateway:
    def __init__(self):
        self.port_tcp1 = 1231
        self.port_tcp2 = 1232
        self.port_tcp3 = 1233
        self.port_udp2 = 1234
        self.port_udp3 = 1235
    
    def connectTcpServer1(self,host="127.0.0.1", port=PORT_TCP1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.connect((host, port))
            server.sendto(b"TCP SERVER 1", (host, port))
            server.close()

    def connectTcpServer2(self,host="127.0.0.2", port=PORT_TCP2):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.connect((host, port))
            server.sendto(b"TCP SERVER 2", (host, port))
            server.close()

    def connectTcpServer3(self,host="127.0.0.3", port=PORT_TCP3):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.connect((host, port))
            server.sendto(b"TCP SERVER 3", (host, port))
            server.close()
            
    def connectUdpServer1( self,host="127.0.0.4", port=PORT_UDP2):
        msgFromClient       = "UDP SERVER 1"
        bytesToSend         = str.encode(msgFromClient +"1")
        serverAddressPort   = (host, port)
        UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        UDPClientSocket.sendto(bytesToSend, serverAddressPort)

    def connectUdpServer2(self,host="127.0.0.5", port=PORT_UDP3):
        msgFromClient       = "UDP SERVER 2"
        bytesToSend         = str.encode(msgFromClient +"1")
        serverAddressPort   = (host, port)
        UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        UDPClientSocket.sendto(bytesToSend, serverAddressPort)
