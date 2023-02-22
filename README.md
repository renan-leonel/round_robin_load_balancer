# Trabalho desenvolvido na disciplina de Sistemas Distribuídos

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