from Coordenada import Coordenada
from Tamanho import Tamanho

class Item:
    def __init__(self, nome:str, raio_interacao:float, ativo = False):
        self.__nome = nome
        self.__area_interacao = raio_interacao
        self.__ativo = ativo
        self.__coord = ''

    def criar(self, coordenada: Coordenada):
        self.__coord = coordenada
        self.__ativo = True
