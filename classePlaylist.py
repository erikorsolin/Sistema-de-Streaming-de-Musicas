class Playlist:
    def __init__(self, nome_playlist, criador, musicas = [], quantidade_musicas=0, duracao_total=(0, 0)):
        self.nome_playlist = nome_playlist # Contém uma string com o título dado à playlist
        self.criador = criador # Contém uma string com o nome do criador
        self.musicas = musicas # Lista de intâncias da classe Musica
        self.quantidade_musicas = quantidade_musicas # É um inteiro que representa a len(self.musicas)
        self.duracao_total = duracao_total # É uma tupla com a soma dos tempos de cada música, segue o formato (minutos, segundos)
    
    def adicionarMusica(self, musica):
        self.musicas.append(musica)

    #def removerMusica(self, musica):


    # Funções setters
    def setNomePlaylist(self, nome_playlist):
        self.nome_playlist = nome_playlist
    def setMusicas(self, musicas):
        self.musicas = musicas
    def setCriador(self, criador):
        self.criador = criador
    def setQuantidade_musicas(self, quantidade_musicas):
        self.quantidade_musicas = quantidade_musicas
    def setDuracao_total(self, duracao_total):
        self.duracao_total = duracao_total
    
    # Funções Getters
    def getNomePlaylist(self):
        return self.nome_playlist
    def getMusicas(self):
        return self.musicas
    def getCriador(self):
        return self.criador
    def getQuantidade_musicas(self):
        return self.quantidade_musicas
    def getDuracao_total(self):
        return self.duracao_total
    

