from Coordenada import Coordenada
from Tamanho import Tamanho

class Item:
    def __init__(self, nome:str):
        self.__nome = nome
        self.__raio_interacao = 30
        self.__ativo = False
        self.__coord = None

    def criar(self, coordenada: Coordenada):
        self.__coord = coordenada
        self.__ativo = True

    @property
    def raio_interacao(self)->float:
        return self.__raio_interacao

    @property
    def coord(self)->Coordenada:
        return self.__coord

    @property
    def ativo(self)->bool:
        return self.__ativo

    @ativo.setter
    def ativo(self, ativo:bool):
        self.__ativo = ativo
