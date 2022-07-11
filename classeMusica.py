class Musica:
    # Função construtora 
    def __init__(self, nome, artista, formato, duracao):
        self.nome = nome
        self.artista = artista
        self.formato = formato
        self.duracao = self.conversorSegundos(duracao)

    # Função para converter o tempo da música
    def conversorSegundos(tempo_min_segundo):
        lista_min_segundo = tempo_min_segundo.split(':')
        tempo_segundos = 0
        for i, w in enumerate(lista_min_segundo):
            if i == 0:
                x = int(w)
                tempo_segundos += (x*60)
            else:
                x = int(w)
                tempo_segundos += x
        return tempo_segundos

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