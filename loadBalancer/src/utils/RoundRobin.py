from typing import List

def RoundRobin(currentServer:int, nServers:int):
    currentServer = (currentServer + 1) % (nServers)
    return currentServer