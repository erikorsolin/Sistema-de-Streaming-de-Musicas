from classeMusica import Musica
from classeUsuario import Usuario

# A classe Artista é uma subclasse de Usuário
class Artista(Usuario):
    def __init__(self, username, senha, nome, sexo, data_nascimento, nome_completo, numero_cartao, codigo_seguranca, data_validade):
        super().__init__(username, senha, nome, sexo, data_nascimento, nome_completo, numero_cartao, codigo_seguranca, data_validade)
        self.seguidores = 0
        self.musicas = []

    # Função para que o artista defina a música usando o console
    def uploadMusica(self):
        print("\nEnvie uma nova música".upper())
        
        # NOME MÚSICA E ARTISTA
        nome_musica = str(input("Nome da música: "))
        while len(nome_musica) == 0:
            nome_musica = str(input("Nome inválido, digite novamente: "))
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

    # Função para imprimir todas as músicas do artista no console
    def imprimirMusicasArtista(self):
        print("\nMúsicas de {}:".format(self.nome).upper())
        for musica in self.musicas:
            nome = musica.getNome()
            duracao = "Duração: {:02d}:{:02d}".format(musica.getDuracao()[0], musica.getDuracao()[1])
            formato = "Formato: {}".format(musica.getFormato())
            string = "{:-<35} | {} | {}".format(nome+" ", duracao, formato)
            print(string)
    
    # Função para que o artista remove uma de suas músicas da plataforma
    def removerMusica(self):
        print("\nExcluir uma música".upper())
        for contador, musica in enumerate(self.musicas):
            nome = musica.getNome()
            duracao = "Duração: {:02d}:{:02d}".format(musica.getDuracao()[0], musica.getDuracao()[1])
            formato = "Formato: {}".format(musica.getFormato())
            string = "{}. {:-<35} | {} | {}".format(contador+1, nome+" ", duracao, formato)
            print(string)

        # O artista escolhe a música que deseja escluir digitando o número dessa música
        indice_musica_escolhida = str(input("Digite o número da música que deseja remover: "))
        while indice_musica_escolhida.isdigit() == False or (int(indice_musica_escolhida)-1 not in range(len(self.musicas))):
            indice_musica_escolhida = str(input("Número inválido, digite novamente: "))
        
        indice_musica_escolhida = int(indice_musica_escolhida) - 1
        print('A música "{}" foi excluída'.format(self.musicas[indice_musica_escolhida].getNome()))
        self.musicas.pop(indice_musica_escolhida)

    # Funções que alteram o atributo self.seguidores
    def aumentarSeguidor(self):
        self.seguidores += 1
    def diminuirSeguidor(self):
        self.seguidores -= 1
    
    # Função para definir uma música passando argumentos, sem ser preciso digitar no console
    def setMusica(self, nome_musica, artista, formato_musica, duracao_musica):
        musica = Musica(nome_musica, artista, formato_musica, duracao_musica)
        self.musicas.append(musica)

    # Funções getters
    def getSeguidores(self):
        return self.seguidores
    def getMusicas(self):
        return self.musicas