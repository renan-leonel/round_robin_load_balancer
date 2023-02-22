from src.controllers import ServersController
from src.gateways import ServerGateway

from src.utils import RoundRobin as rb
from fastapi import FastAPI

app = FastAPI()
serverGateway = ServerGateway.ServerGateway()
serversController = ServersController.ServersController(app, serverGateway)

@app.get("/tcp")
async def getClientTcp(id:int):
    returnMessage = serversController.getClientTcp(id)
    return returnMessage
    
@app.get("/udp")
def getClientUdp(id:str):
    returnMessage = serversController.getClientUdp(id)
    return returnMessage