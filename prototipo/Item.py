from mailbox import NotEmptyError
from xmlrpc.client import Boolean
from Coordenada import Coordenada
from Tamanho import Tamanho

class Item:
    def __init__(self, nome:str, area_interacao:Tamanho, ativo = False):
        self.__nome = nome
        self.__area_interacao = area_interacao
        self.__ativo = ativo
        self.__coord = ''

    def criar(self, coordenada: Coordenada):
        self.__coord = coordenada
        self.__ativo = True