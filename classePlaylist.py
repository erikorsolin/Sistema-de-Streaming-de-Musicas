class Playlist:
    def __init__(self, criador, quantidade_musicas, duracao_total, salvamentos):
        self.criador = criador
        self.quantidade_musicas = quantidade_musicas
        self.duracao_total = duracao_total
        self.salvamentos = salvamentos
    
    # Funções setters
    def setCriador(self, criador):
        self.criador = criador
    def setQuantidade_musicas(self, quantidade_musicas):
        self.quantidade_musicas = quantidade_musicas
    def setDuracao_total(self, duracao_total):
        self.duracao_total = duracao_total
    def setSalvamentos(self, salvamentos):
        self.salvamentos = salvamentos
    
    # Funções Getters
    def getCriador(self):
        return self.criador
    def getQuantidade_musicas(self):
        return self.quantidade_musicas
    def getDuracao_total(self):
        return self.duracao_total
    def getSalvamentos(self):
        return self.salvamentos 
    

