from abc import ABC, abstractmethod

class MeioDePagamento():
    def __init__(self, status):
        self.__status = status

    @abstractmethod
    def processar_pagamento(self):
        pass

    @abstractmethod
    def cancelar_pagamento(self):
        pass

    @abstractmethod
    def gerar_comprovante(self):
        pass

class CartaoCredito(MeioDePagamento):
    def __init__(self, status, numero_cartao):
        super().__init__(status)
        self.__numero_cartao = numero_cartao

    def processar_pagamento(self):
        self.__status = "aprovado"
        return "Pagamento por cartão de crédito"

    def cancelar_pagamento(self):
        self.__status = "Cancelado"

    def gerar_comprovante(self):
        if self.__status == "aprovado":
            return  f"Comprovante gerado para o cartão: {self.__numero_cartao[-5:]}"
        elif self.__status == "Cancelado":
            return f"O pagamento foi cancelado"

class Pix(MeioDePagamento):
    def __init__(self, status, chave_pix):
        super().__init__(status)
        self.__chave_pix = chave_pix

    def processar_pagamento(self):
        self.__status = "Aprovado"
        print(f"Aguarde pagamento para a seguinte chave Pix: {self.__chave_pix}")

    def cancelar_pagamento(self):
        return "A operação Pix não pode ser cancelada"

    def gerar_comprovante(self):
        return "comprovante gerado"

class Boleto(MeioDePagamento):
    def __init__(self, status, codigo_de_barras):
        super().__init__(status)
        self.__codigo_de_barras = codigo_de_barras

    def processar_pagamento(self):
        self.__status = "aprovado"
        return f"Aguardando pagamento para o boleto de código: {self.__codigo_de_barras}"

    def cancelar_pagamento(self):
        self.__status = "cancelado"
        return "Boleto cancelado"

    def gerar_comprovante(self):
        if self.__status == "aprovado":
            return "comprovante gerado"
        if self.__status == "cacelado":
            return "pagamento cancelado"
    