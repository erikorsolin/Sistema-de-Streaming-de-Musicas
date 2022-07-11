from classeUsuario import Usuario

# A classe Ouvinte é uma subclasse de Usuário
class Ouvinte(Usuario):
    def __init__(self, username, senha, nome, sexo, data_nascimento, nome_completo, numero_cartao, codigo_seguranca, data_validade, playlists_salvas=[]):
        super().__init__(username, senha, nome, sexo, data_nascimento, nome_completo, numero_cartao, codigo_seguranca, data_validade, playlists_salvas)
        self.artistas_seguindo = []

    def followArtista(self, lista_artistas): # O argumento lista_artistas é uma lista com todas as intâncias da classe artista
        # Gerar lista de todos os artistas e imprime para o usuário
        print("\nSeguir um artista".upper())
        for contador, artista in enumerate(lista_artistas):
            string = "{}. {}".format(contador+1, artista.getNome())
            print(string)

        # Ouvinte seleciona o índice do artista que deseja seguir
        indice_artista_escolhido = str(input("Digite o número do artista que você deseja seguir: "))
        while indice_artista_escolhido.isdigit() == False or (int(indice_artista_escolhido)-1 not in range(len(self.musicas))):
            indice_artista_escolhido = str(input("Número inválido, digite novamente: "))
        indice_artista_escolhido = int(indice_artista_escolhido) - 1
        
        # Adiciona o artista escolhido na lista de artistas_seguindo
        artista_escolhido = lista_artistas[indice_artista_escolhido]
        print("Você começou a seguir {}".format(artista_escolhido.getNome()))
        self.artistas_seguindo.append()
        
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
            while indice_artista_escolhido.isdigit() == False or (int(indice_artista_escolhido)-1 not in range(len(self.musicas))):
                indice_artista_escolhido = str(input("Número inválido, digite novamente: "))
            indice_artista_escolhido = int(indice_artista_escolhido) - 1

            # Remove o artista escolhido da lista de artistas_seguindo
            artista_escolhido = self.artistas_seguindo[indice_artista_escolhido]
            print("Você deixou de seguir {}".format(self.artistas_seguindo[indice_artista_escolhido].getNome()))
            artista_seguindo.pop(indice_artista_escolhido)

            # Aumenta em 1 o atributo self.seguidores do artista que o ouvinte começou a seguir
            artista_escolhido.diminuirSeguidor()
            
