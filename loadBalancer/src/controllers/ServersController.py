from src.gateways import ServerGateway
from src.utils import RoundRobin as rb
from fastapi import FastAPI

class ServersController:
    
    def __init__(self, app:FastAPI, serverGateway:ServerGateway.ServerGateway):
        self.app = app
        self.next_server_padrao = 0
        self.next_server_tipos_conexao = 1
        self.serverGateway = serverGateway
        self.serversUdp = [self.serverGateway.connectUdpServer1, self.serverGateway.connectUdpServer2]
        self.serversTcp = [self.serverGateway.connectTcpServer1, self.serverGateway.connectTcpServer2, self.serverGateway.connectTcpServer3]
    
    def getClientTcp(self, id:int):
        if(id == 2):
            self.serverGateway.connectTcpServer1()
            return {"message": "Tcp client to server 1", "id": id}
    
        if(id == 1):
            self.serversTcp[self.next_server_tipos_conexao]()
            self.next_server_tipos_conexao = rb.RoundRobin(self.next_server_tipos_conexao, len(self.serversTcp))
            return {"message": "Tcp client RoundRobin", "id": id}
    
    def getClientUdp(self, id:str):

        self.serversUdp[self.next_server_padrao]()
        self.next_server_padrao = rb.RoundRobin(self.next_server_padrao, len(self.serversUdp))
        return {"message": "Udp client RoundRobin", "id": id}