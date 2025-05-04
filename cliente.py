# Classe do cliente
import xmlrpc.client
from classcliente import User

# Menu para escolher a porta do servidor
print("=== MENU DE OPÇÕES ===")
print("1 - Conectar à porta 8000")
print("2 - Conectar à porta 8001")
print("3 - Conectar à porta 8002")

opcao = input("Escolha uma opção (1/2/3): ").strip()

if opcao == '1':
    porta = 8000
elif opcao == '2':
    porta = 8001
elif opcao == '3':
    porta = 8002
else:
    print("Opção inválida. Encerrando o programa.")
    exit()

# Conecta ao servidor com a porta selecionada
server = xmlrpc.client.ServerProxy(f"http://localhost:{porta}", allow_none=True)

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
