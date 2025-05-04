# SERVIDOR FILMES

# server.py
from classcliente import User
import xmlrpc.server

class MyServer:
    def __init__(self):
        # Lista de perguntas
        self.perguntas = [
            {"pergunta": "Que ferramenta o jovem Marty consegue viajar para o passado no primeiro filme de 'De volta para o futuro'?",
             "opcoes": ["A) Um relógio", "B) Um carro", "C) Um avião", "D) Um computador"],
             "resposta": "B"},
            {"pergunta": "O que o Darth Vader fala para Luke Skywalker durante o plot twist do filme 'Star Wars: O Império Contra-Ataca'?",
             "opcoes": ["A) Luke, você perdeu", "B) Luke, você vai se juntar às forças do mal no futuro", "C) Luke, eu já venci essa batalha", "D) Luke, eu sou o seu pai"],
             "resposta": "D"},
            {"pergunta": "Qual é o filme da saga de 'Velozes & Furiosos' que ocorre em Tóquio?",
             "opcoes": ["A) 13", "B) 5", "C) 3", "D) 9"],
             "resposta": "C"},
            {"pergunta": "Em 'Toy Story', qual é o nome do garoto que rouba as bonecas da irmã e que desmonta e remonta todos os brinquedos?",
             "opcoes": ["A) Andy", "B) Bob", "C) Cid", "D) Daniel"],
             "resposta": "C"},
            {"pergunta": "Nos filmes de 'Piratas do Caribe', qual é o nome do navio que Jack Sparrow deseja?",
             "opcoes": ["A) Pérola Negra", "B) Holandês Voador", "C) Titanic", "D) Destruidor de Rochas"],
             "resposta": "A"},
            {"pergunta": "No filme 'A Viagem de Chihiro', o quê a bruxa Yubaba faz com os pais da menina?",
             "opcoes": ["A) Os pais dela desaparecem", "B) Os pais dela são transformados em espíritos", "C) Os pais dela sofrem lavagem cerebral", "D) Os pais dela são transformados em porcos"],
             "resposta": "D"},
            {"pergunta": "No filme 'Wall-E', qual é o nome da empresa responsável pela poluição da Terra e pela criação dos robôs?",
             "opcoes": ["A) AS (Astral Safety)", "B) BnL (Buy n Large)", "C) CnB (Construct & Build)", "D) D&D (Dungeons & Dragons)"],
             "resposta": "B"},
            {"pergunta": "No filme 'Jurassic World', qual é o nome do dinossauro pálido que escapa da jaula?",
             "opcoes": ["A) Indominus Rex", "B) Indoraptor", "C) Tiranossaurus Rex", "D) Paletosaurus"],
             "resposta": "A"},
            {"pergunta": "No filme 'Sexta-Feira 13' de 1980, quantas pessoas falecem?",
             "opcoes": ["A) 10", "B) 5", "C) 7", "D) 2"],
             "resposta": "A"},
            {"pergunta": "No filme 'Como Treinar o seu Dragão', o quê o jovem Soluço entrega ao dragão Banguela para domá-lo?",
             "opcoes": ["A) Um pedaço de carne", "B) Um graveto", "C) Um peixe", "D) Uma sela"],
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

server = xmlrpc.server.SimpleXMLRPCServer(("localhost", 8002), allow_none=True)
server.register_instance(MyServer())
print("Servidor rodando na porta 8002...")
server.serve_forever()
