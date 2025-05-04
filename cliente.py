# Classe do cliente
import xmlrpc.client
from classcliente import User

server = xmlrpc.client.ServerProxy("http://localhost:8000", allow_none=True)
#server = xmlrpc.client.ServerProxy("http://localhost:8001", allow_none=True)
#server = xmlrpc.client.ServerProxy("http://localhost:8002", allow_none=True)

nome_usuario = input("Digite seu nome: ").strip()
user = User(nome_usuario)

while True:
    # Envia o objeto como dicionário (para evitar problemas de serialização)
    response = server.processar_interacao(user.__dict__)

    print(response["mensagem"])

    if response["fim"]:
        break

    # Solicita resposta do usuário, envia novamente
    resposta = input("Sua resposta: ").strip().upper()
    user.resp_cliente = resposta
