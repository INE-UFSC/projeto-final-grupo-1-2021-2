from Coordenada import Coordenada


class PontoEntrega:
    def __init__(self, coord: Coordenada, raio_interacao: float=50):
        self.__coordenada = coord
        self.__raio_interacao = raio_interacao

    # getters

    @property
    def coordenada(self):
        return self.__coordenada

    @property
    def raio_interacao(self):
        return self.__raio_interacao
