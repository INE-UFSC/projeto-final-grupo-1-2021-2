from Mapa import Mapa
from Item import Item


class Biblioteca:
    def __init__(self, mapas: list[Mapa], lista_itens: list[dict[list[Item]]]):
        self.__mapas = mapas
        self.__lista_itens = lista_itens

    def getMapaNivel(self, nivel):
        return self.__mapas[nivel]

    def getItensDificuldade(self, dificuldade):
        return self.__lista_itens[dificuldade]
