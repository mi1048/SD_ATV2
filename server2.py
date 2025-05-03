# SD E PP

# server.py
from classcliente import User
import xmlrpc.server

class MyServer:
    def __init__(self):
        # Lista de perguntas
        self.perguntas = [
            {"pergunta": "O que é um sistema distribuído?",
             "opcoes": ["A) Um sistema rodando em um único processador", "B) Um sistema com múltiplos usuários, mas uma única máquina", "C) Um conjunto de computadores independentes que parecem um sistema único ao usuário", "D) Um tipo de sistema operacional em tempo real"],
             "resposta": "C"}, 
            {"pergunta": "Em sistemas distribuídos, o que é a transparência de localização?",
             "opcoes": ["A) Esconder a identidade dos usuários", "B) Ocultar o local físico de onde os recursos estão", "C)  Sincronizar os relógios dos servidores", "D) Compartilhar senhas entre sistemas"],
             "resposta": "B"},
            {"pergunta": "O que caracteriza uma aplicação paralela?",
             "opcoes": ["A) Múltiplos processos independentes que não se comunicam", "B) Execução sequencial de tarefas com múltiplos usuários", "C) Tarefas divididas e executadas simultaneamente em múltiplos núcleos ou máquinas", "D) Aplicações que só rodam em servidores"],
             "resposta": "C"}, 
            {"pergunta": "Qual das opções abaixo é um benefício da programação paralela?",
             "opcoes": ["A) Maior latência", "B) Redução da escalabilidade", "C) Aumento da eficiência computacional", "D) Diminuição do uso de CPU"],
             "resposta": "C"},
            {"pergunta": "Qual dessas APIs é usada comumente para programação paralela em C/C++?",
             "opcoes": ["A) HTML", "B) MPI", "C) SQL", "D) CSS"],
             "resposta": "B"},
            {"pergunta": "Qual dos itens abaixo é uma desvantagem de sistemas distribuídos?",
             "opcoes": ["A) Maior tolerância a falhas", "B) Escalabilidade", "C) Complexidade na comunicação entre processos", "D) Facilidade de depuração"],
             "resposta": "C"}, 
            {"pergunta": "Em programação paralela, o que significa “condição de corrida” (race condition)?",
             "opcoes": ["A) Quando dois programas competem por velocidade de execução", "B) Quando dois ou mais threads acessam dados compartilhados ao mesmo tempo sem controle adequado", "C) Quando um processo trava outro propositalmente", "D) Quando um processo entra em loop infinito"],
             "resposta": "B"},
            {"pergunta": "Qual estratégia é comum para evitar condição de corrida?",
             "opcoes": ["A) Printf sincronizado", "B) Semáforos e locks", "C) Aumento de threads", "D) Redução de tempo de CPU"],
             "resposta": "B"},
            {"pergunta": "Qual é a principal diferença entre paralelismo e concorrência?",
             "opcoes": ["A) Concorrência é sempre mais rápida que paralelismo", "B) Concorrência simula múltiplas tarefas, paralelismo as executa simultaneamente", "C) Paralelismo é baseado em rede, concorrência em banco de dados", "D) Não existe diferença"],
             "resposta": "B"},
             {"pergunta": "Em sistemas distribuídos, o que é o middleware?",
             "opcoes": ["A) Uma aplicação cliente leve", "B) Um serviço de monitoramento remoto", "C) Um software que facilita a comunicação entre aplicações distribuídas", "D) Um tipo de antivírus distribuído"],
             "resposta": "C"},
            
        ]

    def verify_access(self, user_data):
        user = User(**user_data)

        if user.num_perg >= len(self.perguntas):
            return {"fim": True, "mensagem": f"Fim do quiz. Pontuação: {user.quantidade_pts}"}

        pergunta_atual = self.perguntas[user.num_perg]
        return {
            "fim": False,
            "pergunta": pergunta_atual["pergunta"],
            "opcoes": pergunta_atual["opcoes"],
            "num_perg": user.num_perg,
            "quantidade_pts": user.quantidade_pts
        }

    def responder(self, user_data):
        user = User(**user_data)
        resposta_correta = self.perguntas[user.num_perg]["resposta"]

        resultado = "correta" if user.resp_cliente.upper() == resposta_correta else f"errada! Correta: {resposta_correta}"
        if user.resp_cliente.upper() == resposta_correta:
            user.quantidade_pts += 1

        user.num_perg += 1  # próxima pergunta

        return {
            "resultado": resultado,
            "quantidade_pts": user.quantidade_pts,
            "num_perg": user.num_perg
        }

server = xmlrpc.server.SimpleXMLRPCServer(("localhost", 8001), allow_none=True)
server.register_instance(MyServer())
print("Servidor rodando na porta 8001...")
server.serve_forever()
