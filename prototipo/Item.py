from Coordenada import Coordenada
from Interativos import Interativos
import pygame


class Item(Interativos):
    def __init__(self, nome: str):
        self.__nome = nome
        super().__init__(30)

    def criar(self, coordenada: Coordenada):
        self.coord = coordenada
        self.ativo = True
        self.rect = pygame.Rect(
            self.coord.x, self.coord.y, 14, 14)
        return self

    def desenhar(self, display, posicao_camera):
        cor = (0, 255, 0)  # VERDE
        self.rect.center = (self.coord.x, self.coord.y)
        self.rect.x = self.coord.x - posicao_camera.x
        self.rect.y = self.coord.y - posicao_camera.y
        pygame.draw.rect(display, cor, self.rect)


'''    @ property
    def raio_interacao(self) -> float:
        return self.__raio_interacao

    @ property
    def coord(self) -> Coordenada:
        return self.__coordenada

    @ property
    def ativo(self) -> bool:
        return self.__ativo

    @ ativo.setter
    def ativo(self, ativo: bool):
        self.__ativo = ativo'''
