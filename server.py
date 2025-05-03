# SERVIDOR MATEMÁTICA

# server.py
from classcliente import User
import xmlrpc.server

class MyServer:
    def __init__(self):
        # Lista de perguntas
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
            {"pergunta": "Um elevador pode levar 20 adultos ou 24 crianças. Se 15 adultos já estão no elevador, quantas crianças ainda podem entrar?",
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

server = xmlrpc.server.SimpleXMLRPCServer(("localhost", 8000), allow_none=True)
server.register_instance(MyServer())
print("Servidor rodando na porta 8000...")
server.serve_forever()
