import xmlrpc.client
from classcliente import User
# Solicita ao usuário que digite o nome de usuário e senha
nome_usuario = input("Digite seu nome de usuário: ")
num_perg= input("Digite a pergunta que desaja comecar: ")
# Cria uma instância do Usuario com os dados inseridos
usuario = User(nome_usuario, senha)
# Converte o Usuario para um dicionário antes de enviar
user_data = {'nome_usuario': usuario.nome_usuario,
'senha': usuario.senha}
server = xmlrpc.client.ServerProxy("http://localhost:8000")
 # Envia o objeto Usuario como um dicionário e recebe a resposta do servidor
response = server.verify_access(user_data)
print(response)