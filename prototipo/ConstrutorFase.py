import Biblioteca
import Item
import Mapa
import Fase


class ConstrutorFase:
    def __init__(self, dificuldade : int, mapa : Mapa, lista_itens : list, num_inimigos : int, num_itens : int, nivel : int):
        self.__dificuldade = dificuldade
        self.__mapa = mapa
        self.__lista_itens = lista_itens
        self.__num_inimigos = num_inimigos
        self.__num_itens = num_itens
        self.__nivel = nivel

    #GETTERS
    @property
    def dificuldade(self):
        return self.__dificuldade
    @property
    def mapa(self):
        return self.__mapa
    @property
    def lista_itens(self):
        return self.__lista_itens
    @property
    def num_inimigos(self):
        return self.__num_inimigos
    @property
    def num_itens(self):
        return self.__num_itens
    @property
    def nivel(self):
        return self.__nivel

    #METODO
    def constroiFase(biblioteca : Biblioteca) -> Fase:
        pass
