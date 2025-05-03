# classcliente.py
class User:
    def __init__(self, nome_usuario, quantidade_pts=0, num_perg=0, resp_cliente=""):
        self.nome_usuario = nome_usuario
        self.quantidade_pts = quantidade_pts
        self.num_perg = num_perg
        self.resp_cliente = resp_cliente
