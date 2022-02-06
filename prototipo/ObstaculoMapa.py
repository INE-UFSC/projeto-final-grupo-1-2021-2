from Coordenada import Coordenada
from Tamanho import Tamanho


class ObstaculoMapa:
    def __init__(self, coordenada: Coordenada = '', tamanho: Tamanho = ''):
        self.__coordenada = coordenada
        self.__tamanho = tamanho

    # getters

    @property
    def coordenada(self):
        return self.__coordenada

    @property
    def tamanho(self):
        return self.__tamanho

    # métodos

    def criarDuasCoordenadas(a, b):
        pass
