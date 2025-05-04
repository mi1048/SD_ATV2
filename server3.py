# servidor de FILMES
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
server = ThreadedXMLRPCServer(("localhost", 8002), allow_none=True)
server.register_instance(MyServer())
print("Servidor pronto na porta 8002. Esperando conexões...")
server.serve_forever()
