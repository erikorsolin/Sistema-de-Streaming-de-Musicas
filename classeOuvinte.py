from classeUsuario import Usuario

# A classe Ouvinte é uma subclasse de Usuário
class Ouvinte(Usuario):
    def __init__(self, username, senha, nome, sexo, data_nascimento, nome_completo, numero_cartao, codigo_seguranca, data_validade, playlists_salvas=[]):
        super().__init__(username, senha, nome, sexo, data_nascimento, nome_completo, numero_cartao, codigo_seguranca, data_validade, playlists_salvas)
        self.artista_favorito = None