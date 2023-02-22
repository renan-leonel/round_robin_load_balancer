### Trabalho realizado na disciplina de Sistemas Distribuídos

##### implementação de um balanceador de carga utilizando o algoritmo Round-Robin. Foi criada uma API client/server utilizando FastAPI.

### How to execute

### Install all dependencies
pip install -r requirements.txt

### execute all servers before requesting
##### open "servers" folder and run

python3 serverName.py

### run load balancer

##### in "loadBalancer" folder
python3 -m uvicorn src.main:app --reload

### execute requests 
