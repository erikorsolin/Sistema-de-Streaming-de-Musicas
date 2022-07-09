from multiprocessing.reduction import send_handle


class Usuario:
    def __init__(self, username, senha, nome, sexo, data_nascimento, endereco_monetario, playlists_salvas):
        self.username: username
        self.senha: senha