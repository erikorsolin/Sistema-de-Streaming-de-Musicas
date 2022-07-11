class Musica:
    # Função construtora 
    def __init__(self, nome, artista, formato, duracao):
        self.nome = nome # É uma string com o nome da música
        self.artista = artista # Contém o nome do artista que gerou a música
        self.formato = formato # É uma string "WAV", "MP3" ou "AAC"
        self.duracao = duracao # É uma tupla no formato (mínutos, segundos)

    # Funções setters
    def setNomeCompleto(self, nome):
        self.nome = nome
    def setArtista(self, artista):
        self.artista = artista
    def setFormato(self, formato):
        self.formato = formato
    def setDuracao(self, duracao):
        self.duracao = duracao
    
    # Funções Getters
    def getNome(self):
        return self.nome
    def getArtista(self):
        return self.artista
    def getFormato(self):
        return self.formato
    def getDuracao(self):
        return self.duracao