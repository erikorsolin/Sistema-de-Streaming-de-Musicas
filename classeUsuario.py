from multiprocessing.reduction import send_handle


class Usuario:
    def __init__(self, username, senha, nome, sexo, data_nascimento, endereco_monetario, playlists_salvas):
        self.username = username
        self.senha = senha
        self.nome = nome
        self.sexo = sexo
        self.data_nascimento = data_nascimento
        self.endereco_monetario = endereco_monetario
        self.playlists_salvas = playlists_salvas