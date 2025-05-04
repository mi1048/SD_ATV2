# cliente.py
import xmlrpc.client
from classcliente import User

server = xmlrpc.client.ServerProxy("http://localhost:8000")
# server = xmlrpc.client.ServerProxy("http://localhost:8001")
# server = xmlrpc.client.ServerProxy("http://localhost:8002")

nome_usuario = input("Digite seu nome: ")

quantidade_pts = 0
num_perg = 0
# cliente.py
import xmlrpc.client

server = xmlrpc.client.ServerProxy("http://localhost:8000")
server.iniciar_quiz()
