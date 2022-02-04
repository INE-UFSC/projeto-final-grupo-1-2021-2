import re
from Coordenada import Coordenada
from Tamanho import Tamanho


class PontoEntrega:
    def __init__(self, coord: Coordenada, area_interacao: Tamanho):
        self.__coordenada = coord
        self.__area_interacao = area_interacao

    # getters

    @property
    def coordenada(self):
        return self.__coordenada

    @property
    def area_interacao(self):
        return self.__area_interacao
