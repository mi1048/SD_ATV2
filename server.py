# server.py
from classcliente import User
import xmlrpc.server

class MyServer:
    def __init__(self):
        # Lista de perguntas
        self.perguntas = [
            {"pergunta": "Qual a capital do Brasil?",
             "opcoes": ["A) São Paulo", "B) Rio de Janeiro", "C) Brasília", "D) Salvador", "E) Belo Horizonte"],
             "resposta": "C"},
            {"pergunta": "Quanto é 2 + 2?",
             "opcoes": ["A) 3", "B) 4", "C) 5", "D) 6", "E) 7"],
             "resposta": "B"},
            {"pergunta": "Qual a cor do céu em dia claro?",
             "opcoes": ["A) Azul", "B) Verde", "C) Vermelho", "D) Cinza", "E) Branco"],
             "resposta": "A"},
            # ... até 9 perguntas
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
