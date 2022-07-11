from classeMusica import Musica
from classeUsuario import Usuario

# A classe Artista é uma subclasse de Usuário
class Artista(Usuario):
    def __init__(self, username, senha, nome, sexo, data_nascimento, nome_completo, numero_cartao, codigo_seguranca, data_validade, playlists_salvas=[]):
        super().__init__(username, senha, nome, sexo, data_nascimento, nome_completo, numero_cartao, codigo_seguranca, data_validade, playlists_salvas)
        self.seguidores = None
        self.ranking = None
        self.musicas = []

    def uploadMusica(self):
        print("\nEnvie uma nova música".upper())
        
        # NOME MÚSICA E ARTISTA
        nome_musica = str(input("Nome da música: "))
        artista = self.nome
        
        # FORMATO
        formato_musica = str(input("Formato do arquivo [WAV/MP3/AAC]: ")).upper()
        while formato_musica != "WAV" and formato_musica != "MP3" and formato_musica != "AAC":
            print("Formato de arquivo inválido, digite o formato novamente.")
            formato_musica = str(input("Formato do arquivo [WAV/MP3/AAC]: ")).upper()
        
        # DURAÇÃO
        while True:
            minutos = str(input("Quantos minutos tem essa música? "))
            while minutos.isdigit() == False or int(minutos) > 60 or int(minutos) < 0:
                minutos = str(input("Minutos inválidos, insira o valor novamente: "))
            minutos = int(minutos)

            segundos = str(input("Quantos segundos tem essa música? "))
            while segundos.isdigit() == False or int(segundos) > 60 or int(segundos) < 0:
                segundos = str(input("Segundos inválidos, insira o valor novamente: "))
            segundos = int(segundos)

            if minutos == 0 and segundos == 0:
                print("A música não pode ter 00:00 de duração, insira a duração novamente")
            else:
                duracao_musica = (minutos, segundos) # Envia a duração da música em uma tupla com os minutos e segundos
                break

        musica = Musica(nome_musica, artista, formato_musica, duracao_musica)
        self.musicas.append(musica)

    #def removeMusica():
    
