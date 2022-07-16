from classeOuvinte import Ouvinte
from classeArtista import Artista

# Funções usadas pelo menu

# Retornar True e a Classe do usuário se o nome do usuário estiver registrado no sistema
def usuarioExistente(nome_usuario, lista_usuarios):
    for usuario in lista_usuarios:
        if nome_usuario.lower() == usuario.getUseranme().lower():
            return {"existencia" : True, "user" : usuario}
    return {"existencia" : False, "user" : None} # Retorna se o usuário não foi encontrado na lista

# Todas as opções para se for um usuário logado for Ouvinte
def menuOuvinte(user, lista_artistas):
    while True:
        print("\nMenu de opções para ouvinte".upper())
        print("1. Ver músicas disponíveis")
        print("2. Ver artistas da plataforma")
        print("3. Seguir um artista")
        print("4. Deixar de seguir um artista")
        print("5. Criar uma playlist")
        print("6. Excluir uma playlist")
        print("7. Editar uma playlist")
        print("8. Ver informações do seu cartão de crédito")
        print("9. Deslogar")
        escolha = str(input('Digite o número da opção escolhida: '))
        while escolha.isdigit() == False or (int(escolha)-1 not in range(8)):
            escolha = str(input('Escolha inválida, digite novamente: '))

        if escolha == '1':
            pass

        elif escolha == '9': # Quando a opção 9 (deslogar) for escolhida, a função irá terminar de rodar
            break

# Todas as opções para se for um usuário logado for Artista
def menuArtista(user, lista_artistas):
    while True:
        print("\nMenu de opções para artista".upper())
        print("1. Ver músicas disponíveis")
        print("2. Ver artistas da plataforma")
        print("3. Ver suas estatísticas")
        print("4. Adicionar nova música")
        print("5. Remover uma música")
        print("6. Ver todas suas músicas")
        print("7. Criar uma playlist")
        print("8. Excluir uma playlist")
        print("9. Editar uma playlist")
        print("10. Ver informações do seu cartão de crédito")
        print("11. Deslogar")
        escolha = str(input('Digite o número da opção escolhida: '))
        while escolha.isdigit() == False or (int(escolha)-1 not in range(10)):
            escolha = str(input('Escolha inválida, digite novamente: '))

        if escolha == '1': # Ver músicas disponíveis
            print("\nMúsicas disponíveis na plataforma".upper())
            for artista in lista_artistas:
                lista_musicas = artista.getMusicas()
                for contador, musica in enumerate(lista_musicas):
                    nome_musica = musica.getNome()
                    nome_artista = musica.getArtista()
                    duracao = "Duração: {:02d}:{:02d}".format(musica.getDuracao()[0], musica.getDuracao()[1])
                    print("{}. {:-<35} | {} | {}".format(contador+1, nome_musica+" ", nome_artista, duracao))

        elif escolha == '2': # Ver artistas da plataforma
            print("\nArtistas registrados na plataforma".upper())
            for contador, artista in enumerate(lista_artistas):
                print("{}. {} | Seguidores: {}".format(contador+1, artista.getNome(), artista.getSeguidores()))

        elif escolha == '3': # Ver suas estatísticas
            print("\nEstatísticas de {}".format(user.getNome()).upper())
            print("Seguidores: {}".format(user.getSeguidores))
            print("Músicas: {}".format(len(user.getMusicas())))
        
        elif escolha == '4': # Adicionar nova música
            user.uploadMusica()

        elif escolha == '5': # Remover uma música
            user.removerMusica()

        elif escolha == '6': # Ver todas suas músicas
            user.imprimirMusicasArtista()
        
        elif escolha == '7': # Criar uma playlist
            user.criarPlaylist()
        
        elif escolha == '8': # Excluir uma playlist
            user.excluirPlaylist()
        
        elif escolha == '9': # Editar uma playlist
            user.editarPlaylist()
        
        elif escolha == '10': # Ver informações do seu cartão de crédito
            user.imprimirInformacoesCartao()

        elif escolha == '11': # Quando a opção 11 (deslogar) for escolhida, a função irá terminar de rodar
            break

# Variáveis que armazenam as informações criadas durante a execução do programa
lista_usuarios = []
lista_artistas = []


# Ações do usuário, início do programa propriamente
# Logar em uma conta ou criar uma conta
while True:
    print("\nCadastrar novo usuário ou entrar em uma conta existente".upper())
    nome_usuario = str(input("Nome de usuário: "))

    conferir_existencia = usuarioExistente(nome_usuario, lista_usuarios)
    if conferir_existencia['existencia'] == True: # Logar no usuário
        usuario_logado = conferir_existencia['user']
        menuOuvinte(usuario_logado)

    elif conferir_existencia['existencia'] == False: # Criar um novo usuário
        print("\nCriar um novo usuário".upper())
        print("1. Ouvinte")
        print("2. Artista")
        escolha = str(input('Digite o número do tipo de usuário que deseja criar: '))
        while escolha.isdigit() == False or (int(escolha)-1 not in range(2)):
            escolha = str(input('Escolha inválida, digite novamente: '))

        # Argumentos classe Ouvinte: username, senha, nome, sexo, data_nascimento, nome_completo, numero_cartao, codigo_seguranca, data_validade
        # Argumentos classe Artista: username, senha, nome, sexo, data_nascimento, nome_completo, numero_cartao, codigo_seguranca, data_validade

        print("\nRegistrando novo usuário".upper())
        # Username
        username = nome_usuario.lower()
        # Senha
        senha = input('Informe a senha: ')
        # Nome
        nome = input('Informe o seu nome: ').title()
        # Sexo
        sexo = input('Informe seu sexo [M/F]: ').upper()  
        while sexo != 'F' and sexo != 'M':
            sexo = input('Sexo inválido, digite novamente: ').upper()

        # Data de nascimento
        print("\nInforme sua data de nascimento".upper())
        dia = str(input("Digite seu dia de nascimento: "))
        while dia.isdigit() == False or int(dia) < 1 or int(dia) > 31:
            dia = str(input("Dia inválido, digite novamente: "))
        mes = str(input("Digite seu mês de nascimento: "))
        while mes.isdigit() == False or int(mes) < 1 or int(mes) > 12:
            mes = str(input("Mês inválido, digite novamente: "))
        ano = str(input("Digite seu ano de nascimento: "))
        while ano.isdigit() == False or int(ano) < 1900 or int(ano) > 2022:
            ano = str(input("Ano inválido, digite novamente: "))
        data_nascimento = str(int(dia)) + '/' + str(int(mes)) + '/' + str(int(ano)) # Converter para int elimina 0's desnecessários

        # Informações do cartão
        print("\nDigite as informações do cartão de crédito para a cobrança/depósito")
        nome_completo = input('Nome do titular: ') 
        numero_cartao = input('Número do cartão: ')
        while numero_cartao.isdigit() == False or len(numero_cartao) != 16: # Restrição do numero do cartão (composto por 16 caracteres numéricos)            
            numero_cartao = input('Número inválido, digite novamente: ')
        numero_cartao = int(numero_cartao)
        codigo_seguranca = input('Código de segurança: ')
        while codigo_seguranca.isdigit() == False or len(codigo_seguranca) != 3: # Restrição do código de segurança do cartão             
            codigo_seguranca = input('Código inváido, digite novamente: ')
        codigo_seguranca = int(codigo_seguranca)

        print('\nInforme a validade do cartão (formato: 8/27)'.upper()) # Validade do cartao
        mes = input('Mês: ')
        while mes.isdigit() == False or int(mes) < 1 or int(mes) > 12: # Restrição de mês
            mes = input('Inválido, digite o mês novamente: ')
        ano = input('Ano: ')
        while ano.isdigit() == False or int(ano) < 22 or len(ano) != 2: # Restrição de ano no formato de dois dígitos
            ano = input('Inválido, digite o ano novamente: ')
        data_validade = (mes + '/' + ano)

        # Gerar a classe
        if escolha == '1': # Se a opção de criar conta foi de Ouvinte com as informações coletadas
            usuario_logado = Ouvinte(username, senha, nome, sexo, data_nascimento, nome_completo, numero_cartao, codigo_seguranca, data_validade)
            menuOuvinte(usuario_logado, lista_artistas)

        elif escolha == '2': # Se a opção de criar conta foi de Artista com as informações coletadas
            usuario_logado = Artista(username, senha, nome, sexo, data_nascimento, nome_completo, numero_cartao, codigo_seguranca, data_validade)
            menuArtista(usuario_logado, lista_artistas)