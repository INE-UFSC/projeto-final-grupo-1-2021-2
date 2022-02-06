from Coordenada import Coordenada


class PontoEntrega:
    def __init__(self, coord: Coordenada, raio_interacao: float):
        self.__coordenada = coord
        self.__area_interacao = raio_interacao

    # getters

    @property
    def coordenada(self):
        return self.__coordenada

    @property
    def area_interacao(self):
        return self.__area_interacao
