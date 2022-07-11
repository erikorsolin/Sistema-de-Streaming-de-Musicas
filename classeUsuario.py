from classeCartaoCredito import CartaoCredito
from classeMusica import Musica
from classePlaylist import Playlist

class Usuario:
    def __init__(self, username, senha, nome, sexo, data_nascimento, nome_completo, numero_cartao, codigo_seguranca, data_validade):
        self.username = username
        self.senha = senha
        self.nome = nome
        self.sexo = sexo
        self.data_nascimento = self.converterDataNascimento(data_nascimento) # É um dicionário {'dia': int, 'mes': int, 'ano': int}
        self.endereco_monetario = CartaoCredito(nome_completo, numero_cartao, codigo_seguranca, data_validade) # Recebe a classe CartaoCredito
        self.playlists_criadas = [] # Recebe uma lista vazia na invoção da instância, a lista irá receber valores a partir das ações do usuário
    
    # A função converte a string com a data de nascimento do usuário de "dia/mês/ano" para a tupla de 3 valores (dia, mês, ano)
    def converterDataNascimento(self, string_dia_mes_ano):
        lista_dia_mes_ano = str(string_dia_mes_ano).split("/")
        lista_dia_mes_ano = [int(x) for x in lista_dia_mes_ano]
        dia, mes, ano = lista_dia_mes_ano
        return {'dia' : dia, 'mes' : mes, 'ano' : ano}

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
        self.playlists_criadas = playlist_salvas
    
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
        return self.playlists_criadas 

    # Função para que o usuário crie uma nova playlist e adicione à lista self.playlists_criadas
    def criarPlaylist(self):
        # Restrição; ouvintes podem criar até 2 playlists enquanto artistas podem criar ilimitadas playlists
        # Atingida através do polimorfismo, a classe Ouvinte tem a função criarPlaylist() que limita o máximo de playlists que podem ser criadas
        print("\nCriar uma nova playlist".upper())
        nome_playlist = str(input("Digite o nome da playlist: "))
        criador = self.username
        playlist = Playlist(str(nome_playlist), str(criador))
        print('A playlist "{}" foi criada'.format(nome_playlist))
        self.playlists_criadas.append(playlist) 

    def adicionarMusicaPlaylist(self, lista_artistas):
        # Note que o argumento lista_artistas contém a lista de todas as intâncias da classe Artista (todos os objetos Artista)
        # É preciso passar esse argumento pois a função precisa resgatar todas as músicas armazenadas é as músicas ficam armazenadas dentro do atributo musicas de Artistas
        if len(self.playlists_criadas) == 0: # No caso do usuário não ter nenhuma playlist criada
            print("Você não criou nenhum playlist. Crie uma playlist para poder adicionar músicas.")
        else:
            # Imprime as playlists do usuário para que ele escolha qual irá adicionar a música
            print("\nAdicionar músicas na playlist".upper())
            for contador, playlist in enumerate(self.playlists_criadas):
                print("{}. {}".format(contador+1, playlist.getNomePlaylist()))
            
            # Usuário escolhe em qual playlist ele deseja adicionar músicas
            indice_playlist_escolhida = str(input("Digíte o número da playlist à qual quer adicionar músicas: "))
            while indice_playlist_escolhida.isdigit() == False or (int(indice_playlist_escolhida)-1 not in range(len(self.playlists_criadas))):
                indice_playlist_escolhida = str(input("Número inválido, digite novamente: "))
            indice_playlist_escolhida = int(indice_playlist_escolhida) - 1
            playlist_escolhida = self.playlists_criadas[indice_playlist_escolhida]

            # Imprime todas as músicas disponíveis para serem adicionadas
            print("\nMúsicas disponíveis".upper())
            contador = 1
            todas_musicas = []
            for artista in lista_artistas:
                musicas_artista = artista.getMusicas() # A variável musicas_artista irá conter uma lista de objetos músicas
                for musica in musicas_artista: # A variável musica irá ser o objeto música para cada música da lista de musicas_artista
                    print("{}. {}".format(contador, musica.getNome())) # Imprime no formato: 1. Nome da música
                    todas_musicas.append(musica)
                    contador += 1

            # Usuário deve selecionar quais músicas quer adicionar na playlist
            escolhidas = str(input("Digite o número das músicas que deseja adicionar (separados por espaço): ")).split()
            escolhidas_aceitas = []
            # Restrição de entrada (para que o programa não pare por erro no caso do usuário colocar uma string em escolhidas)
            for entrada in escolhidas:
                if entrada.isdigit() == True and (int(entrada)-1 in range(contador-1)): # Se entrada (um dos números que o usuário colocou) for 
                    escolhidas_aceitas.append(int(entrada)-1)
            
            # Imprime o resultado da operação de adicionar músicas para a playlist
            if len(escolhidas_aceitas) == 0:
                print('Nenhuma música foi adicionada à playlist "{}"'.format(playlist_escolhida.getNomePlaylist()))
            else:
                print("{} músicas foram adicionadas à playlist {}".format(len(escolhidas_aceitas), playlist_escolhida.getNomePlaylist()))

            # O loop adiciona as músicas escolhidas na playlist
            for indice in escolhidas_aceitas:
                playlist_escolhida.adicionarMusica(todas_musicas[indice])

    #def removerMusicaPlaylist(self, ):
