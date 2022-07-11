from classeCartaoCredito import CartaoCredito

class Usuario:
    def __init__(self, username, senha, nome, sexo, data_nascimento, nome_completo, numero_cartao, codigo_seguranca, data_validade, playlists_salvas=[]):
        self.username = username
        self.senha = senha
        self.nome = nome
        self.sexo = sexo
        self.data_nascimento = self.converterDataNascimento(data_nascimento) # É uma tupla de 3 valores (dia, mês, ano)
        self.endereco_monetario = CartaoCredito(nome_completo, numero_cartao, codigo_seguranca, data_validade) # Recebe a classe CartaoCredito
        self.playlists_salvas = playlists_salvas # Recebe uma lista vazia na invoção da instância, a lista irá receber valores a partir das ações do usuário
    
    # A função converte a string com a data de nascimento do usuário de "dia/mês/ano" para a tupla de 3 valores (dia, mês, ano)
    def converterDataNascimento(self, string_dia_mes_ano):
        lista_dia_mes_ano = str(string_dia_mes_ano).split("/")
        lista_dia_mes_ano = [int(x) for x in lista_dia_mes_ano]
        dia, mes, ano = lista_dia_mes_ano
        return (dia, mes, ano)

    # Funções setters
    def setNome(self, nome):
        self.nome = nome
    def setUsername(self, user):
        self.username = user
    def setSenha(self, senha):
        self.senha = senha
    def setSexo(self, sexo):
        self.sexo = sexo
    def setDataNascimento(self, data_nascimento):
        self.data_nascimento = self.converterDataNascimento(data_nascimento)
    def setEnderacoMonetario(self, nome_completo, numero_cartao, codigo_seguranca, data_validade):
        self.endereco_monetario = CartaoCredito(nome_completo, numero_cartao, codigo_seguranca, data_validade)
    def setPlaylistSalvas(self, playlist_salvas):
        self.playlists_salvas = playlist_salvas
    
    # Funções getters
    def getNome(self):
        return self.nome
    def getUsername(self):
        return self.username 
    def getSenha(self):
        return self.senha 
    def getSexo(self):
        return self.sexo 
    def setDataNascimento(self):
        return self.data_nascimento 
    def setEnderacoMonetario(self):
        return self.endereco_monetario
    def setPlaylistSalvas(self):
        return self.playlists_salvas 

    # Função para que o usuário crie uma nova playlist e adicione à lista self.playlists_salvas
    def criarPlaylist(self, ):
        # Restrição; ouvintes podem criar até 4 playlists enquanto artistas podem criar ilimitadas playlists
        if isinstance(self, Ouvinte) and len(self.playlists_salvas) > 4:
            print("Limite de playlists criadas atingindo! Ouvintes podem criar no máximo 4 playlists.")
        else:
            musicas = []
            criador = self.username
            playlist = Playlist(musicas, criador)
            self.playlists_salvas.append(playlist)

    #def adicionarMusicaPlaylist(self, ):


    #def removerMusicaPlaylist(self, ):


    #def salvarPlaylist(self, ):


    #def removerSalvarPlaylist(self, ):