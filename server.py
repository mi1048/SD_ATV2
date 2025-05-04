# QUIZ DE MATEMATICA
from classcliente import User
from socketserver import ThreadingMixIn
from xmlrpc.server import SimpleXMLRPCServer
import threading

# classe que permite que servidor lide com múltiplos clientes ao mesmo tempo
class ThreadedXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
    pass

# classe main
class MyServer:
    def __init__(self):
        self.perguntas = [
            {"pergunta": "Quanto é 2 + 2?",
             "opcoes": ["A) 3", "B) 4", "C) 5", "D) 6"],
             "resposta": "B"},
            {"pergunta": "Quanto é (2 x 2) / (4 - 2)?",
             "opcoes": ["A) 0", "B) 1", "C) 2", "D) 3"],
             "resposta": "C"},
            {"pergunta": "Qual é o valor da função f(x) = -10x - 8 quando x = 2?",
             "opcoes": ["A) -12", "B) 12", "C) -16", "D) -28"],
             "resposta": "D"},
            {"pergunta": "Um elevador pode levar 20 adultos ou 24 crianças. Se 15 adultos já estão no elevador,quantas crianças ainda podem entrar?", 
             "opcoes": ["A) 6", "B) 7", "C) 8", "D) 5"],
             "resposta": "A"},
            {"pergunta": "Qual é a integral de x^2, de 1 até 3?",
             "opcoes": ["A) 27/3", "B) 19/4", "C) 19/3", "D) 26/3"],
             "resposta": "D"},
            {"pergunta": "Pedro tem 30 anos. Se ele tivesse nascido há 10 anos atrás, quantos anos ele teria?",
             "opcoes": ["A) 10", "B) 20", "C) 15", "D) 40"],
             "resposta": "A"},
            {"pergunta": "Resolva o logaritmo log 3 (27,81)",
             "opcoes": ["A) 5", "B) 6", "C) 7", "D) 8"],
             "resposta": "C"},
            {"pergunta": "Informe a derivada em y de 20xy - 37y: ",
             "opcoes": ["A) 20y - 37", "B) 20x - 37", "C) 20xy - 37", "D) 20x - 37y"],
             "resposta": "B"},
        ]

    def iniciar_quiz(self):
        thread = threading.Thread(target=self._executar_quiz)
        thread.start()
        return "Bem vindo ao servidor de perguntas de matematica. Responda no terminal do servidor."

    def _executar_quiz(self):
        nome = input("\n[QUIZ] Digite seu nome: ").strip().upercase
        user = User(nome)

        while user.num_perg < len(self.perguntas):
            pergunta_atual = self.perguntas[user.num_perg]
            print(f"\nPergunta {user.num_perg + 1}: {pergunta_atual['pergunta']}")
            for opcao in pergunta_atual['opcoes']:
                print(opcao)

            resposta = input("Sua resposta: ").strip().upper()
            correta = pergunta_atual['resposta']

            if resposta == correta:
                print("Resposta correta!")
                user.quantidade_pts += 1
            else:
                print(f"Resposta errada! Correta: {correta}")

            user.num_perg += 1

        print(f"\nFim do quiz, {user.nome_usuario}! Você fez {user.quantidade_pts} ponto(s).")

# Inicia o servidor multi-threaded e começa a escutar as conexões dos clientes
server = ThreadedXMLRPCServer(("localhost", 8000), allow_none=True)
server.register_instance(MyServer())
print("Servidor pronto na porta 8000. Esperando conexões...")
server.serve_forever()
