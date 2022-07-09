class CartaoCredito:
    def __init__(self, nome_completo, numero_cartao, codigo_seguranca, data_validade):
        self.nome_completo = str(nome_completo).upper()
        self.numero = numero_cartao
        self.codigo_seguranca = codigo_seguranca
        self.validade = data_validade # CONVERTER DATA DE VALIDADE DE STR PARA UMA TUPLA
    
    # Funções Setters
    def setNomeCompleto(self, nome_completo):
        self.nome_completo = nome_completo
    def setNumeroCartao(self, numero_cartao):
        self.numero = numero_cartao
    def setCodigoSeguranca(self, codigo_seguranca):
        self.codigo_seguranca = codigo_seguranca
    def setValidade(self, data_validade):
        self.validade = data_validade

    # Funções Getters
    def getNomeCompleto(self):
        return self.nome_completo
    def getNumeroCartao(self):
        return self.numero
    def getCodigoSeguranca(self):
        return self.codigo_seguranca
    def getValidade(self):
        return self.validade

    # Função para substituir o cartão de crédito (reúne todos os setters)
    def substituirCartao(self, nome_completo, numero_cartao, codigo_seguranca, data_validade):
        self.nome_completo = str(nome_completo).upper()
        self.numero = numero_cartao
        self.codigo_seguranca = codigo_seguranca
        self.validade = data_validade
    
    def imprimirInformacoesCartao(self):
        # numero_formatado contém o número do cartão de crédito separado por espaços de 4 em 4 dígitos
        numero_formatado = str(self.numero)[0:4] + " " +str(self.numero)[4:8] + " " + str(self.numero)[8:12] + " " + str(self.numero)[12:16]

        print("\nINFORMAÇÕES DO CARTÃO DE CRÉDITO")
        print("{:>9} {:>22}".format("Nome:", self.nome_completo))
        print("{:>9} {:>22}".format("Número:", numero_formatado))
        print("{:>9} {:>22}".format("Validade:", self.codigo_seguranca))
        print("{:>9} {:>22}".format("CVV:", self.validade))