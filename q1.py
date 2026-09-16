from abc import ABC, abstractmethod

class Entrega(ABC):
    def __init__(self, endereco_destino, peso):
        self.__endereco_destino = endereco_destino
        self.__peso = peso
        self.__status = None

    def atualizar_status(self, status):
        self.__status = status

    def imprimir_dados(self):
        return f"Endereço: {self.__endereco_destino}\nPeso: {self.__peso}\nStatus: {self.__status}"

    @abstractmethod
    def calcular_frete(self):
        pass

class EntregaTerrestre(Entrega):
    def __init__(self, endereco_destino, peso, distancia_km):
        super().__init__(endereco_destino, peso)
        self.__distancia_km = distancia_km

    def imprimir_dados(self):
        return super().imprimir_dados() + f"\nDistância: {self.__distancia_km} km"

    def calcular_frete(self):
        if 0 <= self.__distancia_km <= 100:
            return 20
        elif 101 <= self.__distancia_km <= 500:
            return 40 + (self._Entrega__peso / 1.5)
        elif self.__distancia_km > 500:
            return 70 + (self._Entrega__peso / 2.2)
        return 0

class EntregaAerea(Entrega):
    def __init__(self, endereco_destino, peso, taxa_despacho):
        super().__init__(endereco_destino, peso)
        self.__taxa_despacho = taxa_despacho

    def imprimir_dados(self):
        return super().imprimir_dados() + f"\nTaxa de despacho: {self.__taxa_despacho}"

    def calcular_frete(self):
        return self.__taxa_despacho + (self.__peso * 12)





