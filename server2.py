# servidor de SISTEMAS DISTRIBUÍDOS & PROGRAMAÇÃO PARALELA
from classcliente import User
from xmlrpc.server import SimpleXMLRPCServer
from socketserver import ThreadingMixIn
import threading

# cria a classe de multithreads
class ThreadedXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
    pass

class MyServer:
    def __init__(self):
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
        self.usuarios = {}  # Armazena os estados dos usuários
        self.lock = threading.Lock()

    def processar_interacao(self, user_data):
        user = User(**user_data)
        with self.lock:
            if user.nome_usuario not in self.usuarios:
                self.usuarios[user.nome_usuario] = user
                print(f"[INFO] Novo usuário conectado: {user.nome_usuario}")
            else:
                self.usuarios[user.nome_usuario].resp_cliente = user.resp_cliente

            user_atual = self.usuarios[user.nome_usuario]

            # Corrigir resposta se houver
            if user_atual.resp_cliente:
                correta = self.perguntas[user_atual.num_perg]["resposta"]
                if user_atual.resp_cliente.upper() == correta:
                    user_atual.quantidade_pts += 1
                    resultado = "correta"
                else:
                    resultado = f"errada! A resposta correta era: {correta}"
                user_atual.num_perg += 1
                user_atual.resp_cliente = None  # limpa após uso

                if user_atual.num_perg >= len(self.perguntas):
                    mensagem = f"Você respondeu: {user.resp_cliente.upper()} -> {resultado}\nFim do quiz. {user_atual.nome_usuario}, sua pontuação final foi: {user_atual.quantidade_pts} de {len(self.perguntas)}."
                    print(f"[INFO] Finalizando sessão do usuário: {user_atual.nome_usuario}")
                    del self.usuarios[user.nome_usuario]
                    return {
                        "mensagem": mensagem,
                        "fim": True
                    }

                # Ainda há perguntas
                proxima = self.perguntas[user_atual.num_perg]
                return {
                    "mensagem": f"Você respondeu: {user.resp_cliente.upper()} -> {resultado}\n\nPergunta {user_atual.num_perg + 1}: {proxima['pergunta']}\n" + "\n".join(proxima['opcoes']),
                    "fim": False,
                    "quantidade_pts": user_atual.quantidade_pts,
                    "num_perg": user_atual.num_perg
                }

            # Se não há resposta, verificar se é fim
            if user_atual.num_perg >= len(self.perguntas):
                mensagem = f"Fim do quiz. {user_atual.nome_usuario}, sua pontuação final foi: {user_atual.quantidade_pts} de {len(self.perguntas)}."
                print(f"[INFO] Finalizando sessão do usuário: {user_atual.nome_usuario}")
                del self.usuarios[user.nome_usuario]
                return {
                    "mensagem": mensagem,
                    "fim": True
                }

            # Enviar nova pergunta
            pergunta = self.perguntas[user_atual.num_perg]
            return {
                "mensagem": f"\nPergunta {user_atual.num_perg + 1}: {pergunta['pergunta']}\n" + "\n".join(pergunta['opcoes']),
                "fim": False,
                "quantidade_pts": user_atual.quantidade_pts,
                "num_perg": user_atual.num_perg
            }

# inicia o server na porta e escuta
server = ThreadedXMLRPCServer(("localhost", 8001), allow_none=True)
server.register_instance(MyServer())
print("Servidor pronto na porta 8001. Esperando conexões...")
server.serve_forever()
