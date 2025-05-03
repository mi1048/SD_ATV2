# cliente.py
import xmlrpc.client
from classcliente import User

server = xmlrpc.client.ServerProxy("http://localhost:8000")
# server = xmlrpc.client.ServerProxy("http://localhost:8001")
# server = xmlrpc.client.ServerProxy("http://localhost:8002")

nome_usuario = input("Digite seu nome: ")

quantidade_pts = 0
num_perg = 0

while True:
    user = User(nome_usuario, quantidade_pts, num_perg)
    user_data = {
        "nome_usuario": user.nome_usuario,
        "quantidade_pts": user.quantidade_pts,
        "num_perg": user.num_perg,
        "resp_cliente": ""
    }

    response = server.verify_access(user_data)

    if response["fim"]:
        print(response["mensagem"])
        break

    print(f"\nPergunta {response['num_perg'] + 1}: {response['pergunta']}")
    for opcao in response["opcoes"]:
        print(opcao)

    resposta = input("Digite sua resposta (A, B, C, ou D): ").strip().upper()

    # Atualiza com a resposta do cliente
    user_data["resp_cliente"] = resposta
    resposta_server = server.responder(user_data)

    print(f"Você respondeu: {resposta} -> Resposta {resposta_server['resultado']}")
    quantidade_pts = resposta_server["quantidade_pts"]
    num_perg = resposta_server["num_perg"]
