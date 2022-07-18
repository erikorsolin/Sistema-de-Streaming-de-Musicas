from classeUsuario import Usuario
from classePlaylist import Playlist

# A classe Ouvinte é uma subclasse de Usuário
class Ouvinte(Usuario):
    def __init__(self, username, senha, nome, sexo, data_nascimento, nome_completo, numero_cartao, codigo_seguranca, data_validade):
        super().__init__(username, senha, nome, sexo, data_nascimento, nome_completo, numero_cartao, codigo_seguranca, data_validade)
        self.artistas_seguindo = []
        self.limite_playlists = 2

    # Funções setters
    def setLimitePlaylists(self, limite_playlists):
        self.limite_playlists = limite_playlists
    
    # Funções Getters
    def getLimitePlaylists(self):
        return self.limite_playlists

    def followArtista(self, lista_artistas): # O argumento lista_artistas é uma lista com todas as intâncias da classe artista
        # Gerar lista de todos os artistas e imprime para o usuário
        print("\nSeguir um artista".upper())
        for contador, artista in enumerate(lista_artistas):
            string = "{}. {}".format(contador+1, artista.getNome())
            print(string)

        # Ouvinte seleciona o índice do artista que deseja seguir
        indice_artista_escolhido = str(input("Digite o número do artista que você deseja seguir: "))
        while indice_artista_escolhido.isdigit() == False or (int(indice_artista_escolhido)-1 not in range(len(lista_artistas))):
            indice_artista_escolhido = str(input("Número inválido, digite novamente: "))
        indice_artista_escolhido = int(indice_artista_escolhido) - 1
        
        # Adiciona o artista escolhido na lista de artistas_seguindo
        artista_escolhido = lista_artistas[indice_artista_escolhido]

        # Confere se o usuário já não segue esse artista
        if artista_escolhido in self.artistas_seguindo:
            print("Você já segue esse artista")
        else:
            print("Você começou a seguir {}".format(artista_escolhido.getNome()))
            self.artistas_seguindo.append(artista_escolhido) # Adiciona o artista que passou a seguir na lista de artistas seguindos

            # Aumenta em 1 o atributo self.seguidores do artista que o ouvinte começou a seguir
            artista_escolhido.aumentarSeguidor()

    def unfollowArtista(self):
        if len(self.artistas_seguindo) == 0: # No caso de o ouvinte não seguir nenhum artista
            print("Você não segue nenhum artista!")
        else: 
            # Imprime todos os artistas que o ouvinte segue
            print("\nDeixar de seguir um artista".upper())
            for contador, artista_seguindo in enumerate(self.artistas_seguindo):
                string = "{}. {}".format(contador+1, artista_seguindo.getNome())
                print(string)
            
            # Ouvinte seleciona o índice do artista que deseja deixar de seguir
            indice_artista_escolhido = str(input("Digite o número do artista que você deseja deixar de seguir: "))
            while indice_artista_escolhido.isdigit() == False or (int(indice_artista_escolhido)-1 not in range(len(self.artistas_seguindo))):
                indice_artista_escolhido = str(input("Número inválido, digite novamente: "))
            indice_artista_escolhido = int(indice_artista_escolhido) - 1

            # Remove o artista escolhido da lista de artistas_seguindo
            artista_escolhido = self.artistas_seguindo[indice_artista_escolhido]
            print("Você deixou de seguir {}".format(self.artistas_seguindo[indice_artista_escolhido].getNome()))
            self.artistas_seguindo.pop(indice_artista_escolhido)

            # Aumenta em 1 o atributo self.seguidores do artista que o ouvinte começou a seguir
            artista_escolhido.diminuirSeguidor()
    
    def criarPlaylist(self):
        # Restrição; ouvintes podem criar até 2 playlists enquanto artistas podem criar ilimitadas playlists
        if len(self.playlists_criadas) >= self.limite_playlists:
            print("\nAviso".upper())
            print("Limite de playlists criadas atingindo! Ouvintes podem criar no máximo 2 playlists.")
        else:
            print("\nCriar uma nova playlist".upper())
            nome_playlist = str(input("Digite o nome da playlist: "))
            criador = self.username
            playlist = Playlist(str(nome_playlist), str(criador))
            print('A playlist "{}" foi criada'.format(nome_playlist))
            self.playlists_criadas.append(playlist) 
