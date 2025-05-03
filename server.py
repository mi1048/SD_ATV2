from user import User
import xmlrpc.server

class MyServer:
 def verify_access(self, user_data):

    # Reconstrói o objeto Usuario a partir do dicionário recebido
    user = User(user_data['nome_usuario'], user_data['quantidade_pts'], user_data['num_perg'], user_data['resp_cliente'])

    int perg_server

    #Verificar qual a pergunta atual
    def escolher_opcao(perg_server):
       
    if perg_server == 1:
        return "Você escolheu 1"
    elif perg_server == 2:
        return "Você escolheu 2"
    elif perg_server == 3:
        return "Você escolheu 3"
    elif perg_server == 1:
        return "Você escolheu 4"
    elif perg_server == 2:
        return "Você escolheu 5"
    elif perg_server == 3:
        return "Você escolheu 6"
    elif perg_server == 1:
        return "Você escolheu 7"
    elif perg_server == 2:
        return "Você escolheu 8"
    elif perg_server == 3:
        return "Você escolheu 9"
    else:
        return "Opção inválida"

    #voltar a proxima pergunta 
    
    

    # Verificar a pergunta atual
    if user.num_perg == perg_server:
      

    # Verifica a senha
    ##if user.senha == "1234":
##return "Acesso permitido"
##else:
##return "Acesso negado"

server = xmlrpc.server.SimpleXMLRPCServer(("localhost", 8000),
allow_none=True)
server.register_instance(MyServer())
server.serve_forever()