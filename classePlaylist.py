class Playlist:
    def __init__(self, nome_playlist, criador):
        self.nome_playlist = nome_playlist # Contém uma string com o título dado à playlist
        self.criador = criador # Contém uma string com o nome do criador
        self.musicas = [] # Lista de intâncias da classe Musica, por padrão é uma lista vazia
        self.quantidade_musicas = 0 # Por padrão é 0 e irá mudar conforme as músicas forem acrescentadas e removidas
    
    def adicionarMusica(self, musica): # Adiciona uma música de cada vez
        if musica not in self.musicas: # Se a música já estiver na playlist, não irá acontecer nada
            self.musicas.append(musica)

            # Atualiza o atributo quantidade_musicas
            self.quantidade_musicas += 1

    def removerMusicas(self, lista_musicas_escolhidas): # O argumento lista_musicas_escolhidas recebe uma lista com as músicas escolhida
        indices_para_remover = []
        for indice, musica in enumerate(self.musicas):
            if musica in lista_musicas_escolhidas:
                indices_para_remover.append(indice)
        indices_para_remover = sorted(indices_para_remover, reverse = True)
        for indice in indices_para_remover:
            self.musicas.pop(indice)
        
        # Atualiza o atributo quantidade_musicas
        self.quantidade_musicas -= len(indices_para_remover)

    # Funções setters
    def setNomePlaylist(self, nome_playlist):
        self.nome_playlist = nome_playlist
    def setCriador(self, criador):
        self.criador = criador
    def setMusicas(self, musicas):
        self.musicas = musicas
    def setQuantidadeMusicas(self, quantidade_musicas):
        self.quantidade_musicas = quantidade_musicas
    
    # Funções Getters
    def getNomePlaylist(self):
        return self.nome_playlist
    def getCriador(self):
        return self.criador
    def getMusicas(self):
        return self.musicas
    def getQuantidadeMusicas(self):
        return self.quantidade_musicas
