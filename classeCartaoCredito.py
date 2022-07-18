class CartaoCredito:
    def __init__(self, nome_completo, numero_cartao, codigo_seguranca, data_validade):
        self.nome_completo = str(nome_completo).upper() # É uma string
        self.numero = numero_cartao # É um inteiro com exatamente 16 dígitos
        self.codigo_seguranca = codigo_seguranca # É um inteiro com 3 dígitos
        self.validade = self.converterValidade(data_validade) # É uma tupla no formato (mês, ano)

    # Converte a data de validade recebida de uma string "mês/ano" para uma tupla (mês, ano)
    def converterValidade(self, string_mes_ano):
        lista_mes_ano = str(string_mes_ano).split("/")
        lista_mes_ano = [int(x) for x in lista_mes_ano]
        return (lista_mes_ano[0], lista_mes_ano[1])
    
    # Função para substituir o cartão de crédito (reúne todos os setters)
    def substituirCartao(self, nome_completo, numero_cartao, codigo_seguranca, data_validade):
        self.nome_completo = str(nome_completo).upper()
        self.numero = numero_cartao
        self.codigo_seguranca = codigo_seguranca
        self.validade = self.converterValidade(data_validade)
    
    # Função que imprime os atributos de forma organizada
    def imprimirInformacoesCartao(self):
        # numero_formatado contém o número do cartão de crédito separado por espaços de 4 em 4 dígitos
        numero_formatado = str(self.numero)[0:4] + " " +str(self.numero)[4:8] + " " + str(self.numero)[8:12] + " " + str(self.numero)[12:16]
        # validade_formatada gera a string "mês/ano" a partir da tupla (mês, ano)
        validade_formatada = str(self.validade[0]) + "/" + str(self.validade[1])

        print("\nINFORMAÇÕES DO CARTÃO DE CRÉDITO")
        print("{:>9} {:>22}".format("Nome:", self.nome_completo))
        print("{:>9} {:>22}".format("Número:", numero_formatado))
        print("{:>9} {:>22}".format("Validade:", self.codigo_seguranca))
        print("{:>9} {:>22}".format("CVV:", validade_formatada))
    
    # Funções Setters
    def setNomeCompleto(self, nome_completo):
        self.nome_completo = nome_completo
    def setNumeroCartao(self, numero_cartao):
        self.numero = numero_cartao
    def setCodigoSeguranca(self, codigo_seguranca):
        self.codigo_seguranca = codigo_seguranca
    def setValidade(self, data_validade):
        self.validade = self.converterValidade(data_validade)

    # Funções Getters
    def getNomeCompleto(self):
        return self.nome_completo
    def getNumeroCartao(self):
        return self.numero
    def getCodigoSeguranca(self):
        return self.codigo_seguranca
    def getValidade(self):
        return self.validade