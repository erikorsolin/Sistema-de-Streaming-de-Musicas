class Usuario:
    def __init__(self, username, senha, nome, sexo, data_nascimento, endereco_monetario, playlists_salvas):
        self.username = username
        self.senha = senha
        self.nome = nome
        self.sexo = sexo
        self.data_nascimento = data_nascimento
        self.endereco_monetario = endereco_monetario
        self.playlists_salvas = playlists_salvas

    # Funções setters
    def setNome(self, nome):
        self.nome = nome
    def setUsername(self, user):
        self.username = user
    def setSenha(self, senha):
        self.senha = senha
    def setSexo(self, sexo):
        self.sexo = sexo
    def setData_nascimento(self, data_nascimento):
        self.data_nascimento = data_nascimento
    def setEnderaco_monetario(self, endereco_monetario):
        self.endereco_monetario = endereco_monetario
    def setPlaylist_salvas(self, playlist_salvas):
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
    def getData_nascimento(self):
        return self.data_nascimento 
    def getEnderaco_monetario(self):
        return self.endereco_monetario
    def getPlaylist_salvas(self):
        return self.playlists_salvas 
    
    