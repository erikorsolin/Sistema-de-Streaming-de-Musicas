from classeUsuario import Usuario

# A classe Artista é uma subclasse de Usuário
class Artista(Usuario):
    def __init__(self, username, senha, nome, sexo, data_nascimento, nome_completo, numero_cartao, codigo_seguranca, data_validade, playlists_salvas=[]):
        super().__init__(username, senha, nome, sexo, data_nascimento, nome_completo, numero_cartao, codigo_seguranca, data_validade, playlists_salvas)
        self.seguidores = None
        self.ranking = None