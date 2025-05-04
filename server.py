# server de METAMATICA
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
            {"pergunta": "Quanto é 2 + 2?", "opcoes": ["A) 3", "B) 4", "C) 5", "D) 6"], "resposta": "B"},
            {"pergunta": "Quanto é (2 x 2) / (4 - 2)?", "opcoes": ["A) 0", "B) 1", "C) 2", "D) 3"], "resposta": "C"},
            {"pergunta": "Qual é o valor da função f(x) = -10x - 8 quando x = 2?", "opcoes": ["A) -12", "B) 12", "C) -16", "D) -28"], "resposta": "D"},
            {"pergunta": "Um elevador pode levar 20 adultos ou 24 crianças. Se 15 adultos já estão no elevador, quantas crianças ainda podem entrar?", "opcoes": ["A) 6", "B) 7", "C) 8", "D) 5"], "resposta": "A"},
            {"pergunta": "Qual é a integral de x^2, de 1 até 3?", "opcoes": ["A) 27/3", "B) 19/4", "C) 19/3", "D) 26/3"], "resposta": "D"},
            {"pergunta": "Pedro tem 30 anos. Se ele tivesse nascido há 10 anos atrás, quantos anos ele teria?", "opcoes": ["A) 10", "B) 20", "C) 15", "D) 40"], "resposta": "A"},
            {"pergunta": "Resolva o logaritmo log 3 (27,81)", "opcoes": ["A) 5", "B) 6", "C) 7", "D) 8"], "resposta": "C"},
            {"pergunta": "Informe a derivada em y de 20xy - 37y:", "opcoes": ["A) 20y - 37", "B) 20x - 37", "C) 20xy - 37", "D) 20x - 37y"], "resposta": "B"},
        ]
        self.usuarios = {}  # Estados por usuário
        self.lock = threading.Lock()

    def processar_interacao(self, user_data):
        user = User(**user_data)

        with self.lock:
            if user.nome_usuario not in self.usuarios:
                self.usuarios[user.nome_usuario] = user
            else:
                self.usuarios[user.nome_usuario].resp_cliente = user.resp_cliente

            usuario = self.usuarios[user.nome_usuario]

            # Se usuário respondeu à pergunta anterior
            if usuario.resp_cliente:
                correta = self.perguntas[usuario.num_perg]["resposta"]
                if usuario.resp_cliente.upper() == correta:
                    usuario.quantidade_pts += 1
                    resultado = "correta"
                else:
                    resultado = f"errada! A resposta correta era: {correta}"

                usuario.num_perg += 1
                usuario.resp_cliente = None

                # Verifica se ainda tem perguntas
                if usuario.num_perg >= len(self.perguntas):
                    return {
                        "mensagem": f"Você respondeu: {user.resp_cliente.upper()} -> {resultado}\nFim do quiz. Pontuação final: {usuario.quantidade_pts}/{len(self.perguntas)}.",
                        "fim": True
                    }

                # Continua para próxima pergunta
                proxima = self.perguntas[usuario.num_perg]
                return {
                    "mensagem": f"Você respondeu: {user.resp_cliente.upper()} -> {resultado}\n\nPergunta {usuario.num_perg + 1}: {proxima['pergunta']}\n" +
                                "\n".join(proxima["opcoes"]),
                    "fim": False
                }

            # Nenhuma resposta ainda, envia primeira pergunta
            if usuario.num_perg >= len(self.perguntas):
                return {
                    "mensagem": f"Fim do quiz. Pontuação final: {usuario.quantidade_pts}/{len(self.perguntas)}.",
                    "fim": True
                }

            pergunta = self.perguntas[usuario.num_perg]
            return {
                "mensagem": f"\nPergunta {usuario.num_perg + 1}: {pergunta['pergunta']}\n" + "\n".join(pergunta["opcoes"]),
                "fim": False
            }

# Inicialização do servidor e escuta
server = ThreadedXMLRPCServer(("localhost", 8000), allow_none=True)
server.register_instance(MyServer())
print("Servidor pronto na porta 8000. Esperando conexões...")
server.serve_forever()
