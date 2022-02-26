from Coordenada import Coordenada
from Tamanho import Tamanho
import pygame


class ObstaculoMapa:
    def __init__(self, coordenada: Coordenada = '', tamanho: Tamanho = ''):
        self.__coord = coordenada
        self.__tamanho = tamanho
        self.__rect = pygame.Rect((self.coord.x, self.coord.y, int(
            self.tamanho.largura), int(self.tamanho.altura)))

    # getters

    @property
    def coord(self):
        return self.__coord

    @property
    def tamanho(self):
        return self.__tamanho

    @property
    def rect(self):
        return self.__rect

    # métodos

    def criarDuasCoordenadas(a, b):
        pass

    def desenhar(self, display, posicao_camera):
        cor = (47, 79, 79)  # cinza escuro
        self.__rect.x = self.coord.x - posicao_camera.x
        self.__rect.y = self.coord.y - posicao_camera.y
        pygame.draw.rect(display, cor, self.__rect)
