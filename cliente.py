# cliente.py
import xmlrpc.client
from classcliente import User

server = xmlrpc.client.ServerProxy("http://localhost:8000")
# server = xmlrpc.client.ServerProxy("http://localhost:8001")
# server = xmlrpc.client.ServerProxy("http://localhost:8002")



server = xmlrpc.client.ServerProxy("http://localhost:8000")
print(server.iniciar_quiz())
