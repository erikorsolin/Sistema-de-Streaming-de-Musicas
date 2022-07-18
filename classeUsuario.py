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
    def setPlaylistSalvas(self, playlists_criadas):
        self.playlists_criadas = playlists_criadas
    
    # Funções getters
    def getNome(self):
        return self.nome
    def getUsername(self):
        return self.username 
    def getSenha(self):
        return self.senha 
    def getSexo(self):
        return self.sexo 
    def getDataNascimento(self):
        return self.data_nascimento 
    def getEnderacoMonetario(self):
        return self.endereco_monetario
    def getPlaylistSalvas(self):
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

    # Função para que o usuário exclua uma playlist criada
    def excluirPlaylist(self):
        if len(self.playlists_criadas) == 0:
            print("Você não criou nenhuma playlist.")
        else:
            # Imprime todas as playlists dos usuário
            print("\nExcluir uma playlist")
            for contador, playlist in enumerate(self.playlists_criadas):
                print("{}. {}".format(contador+1, playlist.getNomePlaylist()))

            # Recebe a entrada do usuário
            escolhida = str(input("Digite o número da playlist que deseja excluir: "))
            while escolhida.isdigit() == False or (int(escolhida)-1 not in range(len(self.playlists_criadas))):
                escolhida = str(input("Número inválido, digite novamente: "))
            indice_escolhida = int(escolhida)-1

            # Remove a playlist escolhida
            self.playlists_criadas.pop(indice_escolhida)

    # A função editarPlaylist permite adicionar ou remover músicas de uma playlist
    def editarPlaylist(self, lista_artistas):
        # Note que o argumento lista_artistas contém a lista de todas as intâncias da classe Artista (todos os objetos Artista)
        # É preciso passar esse argumento pois a função precisa resgatar todas as músicas armazenadas é as músicas ficam armazenadas dentro do atributo musicas de Artistas
        if len(self.playlists_criadas) == 0: # No caso do usuário não ter nenhuma playlist criada
            print("Você não criou nenhuma playlist. Crie uma playlist para poder adicionar músicas.")
        else:
            # Imprime as playlists do usuário para que ele escolha qual irá editar 
            print("\nEditar playlist".upper())
            for contador, playlist in enumerate(self.playlists_criadas):
                print("{}. {}".format(contador+1, playlist.getNomePlaylist()))
            
            # Usuário escolhe qual playlist ele deseja editar
            indice_playlist_escolhida = str(input("Digíte o número da playlist à qual quer editar: "))
            while indice_playlist_escolhida.isdigit() == False or (int(indice_playlist_escolhida)-1 not in range(len(self.playlists_criadas))):
                indice_playlist_escolhida = str(input("Número inválido, digite novamente: "))
            indice_playlist_escolhida = int(indice_playlist_escolhida) - 1
            playlist_escolhida = self.playlists_criadas[indice_playlist_escolhida]

            # Usuário escolhe se irá adicionar ou remover músicas da playlist escolhida
            print("\nAções possíveis".upper())
            print("1. Adicionar músicas à playlist")
            print("2. Remover músicas da playlist")
            entrada = str(input("Digite o número da opção escolhida: "))
            while entrada.isdigit() == False or (int(entrada)-1 not in range(2)):
                entrada = str(input("Número inválido, digite novamente: "))

            if entrada == '1': # Opção de adicionar músicas
                # Imprime todas as músicas disponíveis para serem adicionadas
                print("\nMúsicas disponíveis".upper())
                contador = 1
                todas_musicas = []
                for artista in lista_artistas:
                    musicas_artista = artista.getMusicas() # A variável musicas_artista irá conter uma lista de objetos músicas
                    for musica in musicas_artista: # A variável musica irá ser o objeto música para cada música da lista de musicas_artista
                        print("{}. {} | {}".format(contador, musica.getNome(), musica.getArtista())) # Imprime no formato: 1. 'Nome da música' | 'Nome artista'
                        todas_musicas.append(musica)
                        contador += 1

                # Usuário deve selecionar quais músicas quer adicionar na playlist
                escolhidas = str(input("Digite o número das músicas que deseja adicionar (separados por espaço): ")).split()
                escolhidas_aceitas = []
                # Restrição de entrada (para que o programa não pare por erro no caso do usuário colocar uma string em escolhidas)
                for entrada in escolhidas:
                    if entrada.isdigit() == True and (int(entrada)-1 in range(contador-1)):
                        escolhidas_aceitas.append(int(entrada)-1)

                # Imprime o resultado da operação de adicionar músicas para a playlist
                if len(escolhidas_aceitas) == 0:
                    print('Nenhuma música foi adicionada à playlist "{}"'.format(playlist_escolhida.getNomePlaylist()))
                else:
                    print("> {} músicas foram adicionadas à playlist {}".format(len(escolhidas_aceitas), playlist_escolhida.getNomePlaylist()))

                # O loop adiciona as músicas escolhidas na playlist
                for indice in escolhidas_aceitas:
                    playlist_escolhida.adicionarMusica(todas_musicas[indice])
            
            elif entrada == '2': # Opção de remover músicas
                if len(playlist_escolhida.getMusicas()) == 0: # No caso da playlist selecionada não ter nenhuma música
                    print("\nA playlist selecionada não tem nenhuma música.")
                else:
                    # Imprime todas as músicas da playlist
                    print("\nMúsicas na playlist".upper())
                    musicas_na_playlist = []
                    for contador, musica in enumerate(playlist_escolhida.getMusicas()):
                        print("{}. {} | {}".format(contador+1, musica.getNome(), musica.getArtista()))
                        musicas_na_playlist.append(musica)

                    # Usuário escolhe os números das músicas as quais deseja remover
                    escolhidas = str(input("Digite o número das músicas que deseja remover (separados por espaço): ")).split()
                    escolhidas_aceitas = []
                    # Restrição de entrada (para que o programa não pare por erro no caso do usuário colocar uma string em escolhidas)
                    for entrada in escolhidas:
                        if entrada.isdigit() == True and (int(entrada)-1 in range(len(musicas_na_playlist))): 
                            escolhidas_aceitas.append(int(entrada)-1)
                    
                    # Imprime o resultado da operação de adicionar músicas para a playlist
                    if len(escolhidas_aceitas) == 0:
                        print('Nenhuma música foi removida da playlist "{}"'.format(playlist_escolhida.getNomePlaylist()))
                    else:
                        print("> {} músicas foram removidas da playlist {}".format(len(escolhidas_aceitas), playlist_escolhida.getNomePlaylist()))

                    # Passa as músicas escolhidas em uma lista como argumento para a função removerMusicas()
                    lista_musicas_escolhidas = []
                    for indice in escolhidas_aceitas:
                        lista_musicas_escolhidas.append(playlist_escolhida.getMusicas()[indice])
                    playlist_escolhida.removerMusicas(lista_musicas_escolhidas)
            
    # A função imprime as informações das playlists criadas pelo usuário
    def imprimirPlaylists(self):
        if len(self.playlists_criadas) == 0: # No caso do usuário não ter nenhuma playlist criada
            print("Você não criou nenhuma playlist. Crie uma playlist antes de executar esse comando.")
        else:
            # Imprime as playlists do usuário e suas informações
            for playlist in self.playlists_criadas:
                print("\n> Nome da playlist: {} | Quantidade de músicas: {} | Criador: {}".format(playlist.getNomePlaylist(), playlist.getQuantidadeMusicas(), playlist.getCriador()))
                for contador, musica in enumerate(playlist.getMusicas()):
                    print("{}. {} | {} | {:02d}:{:02d}".format(contador+1, musica.getNome(), musica.getArtista(), musica.getDuracao()[0], musica.getDuracao()[1]))