from Coordenada import Coordenada
from Tamanho import Tamanho
import pygame


class Item:
    def __init__(self, nome: str):
        self.__nome = nome
        self.__raio_interacao = 30
        self.__ativo = False
        self.__coord = None
        self.__rect = None

    def criar(self, coordenada: Coordenada):
        self.__coord = coordenada
        self.__ativo = True
        self.__rect = pygame.Rect(self.coord.x, self.coord.y, 14, 14)

    @ property
    def raio_interacao(self) -> float:
        return self.__raio_interacao

    @ property
    def coord(self) -> Coordenada:
        return self.__coord

    @ property
    def ativo(self) -> bool:
        return self.__ativo

    @ ativo.setter
    def ativo(self, ativo: bool):
        self.__ativo = ativo

    def desenhar(self, display):
        cor = (0, 255, 0)  # VERDE
        pygame.draw.rect(display, cor, self.__rect)
