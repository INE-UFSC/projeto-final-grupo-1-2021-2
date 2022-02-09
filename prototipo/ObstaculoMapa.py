from Coordenada import Coordenada
from Tamanho import Tamanho
import pygame


class ObstaculoMapa:
    def __init__(self, coordenada: Coordenada = '', tamanho: Tamanho = ''):
        self.__coordenada = coordenada
        self.__tamanho = tamanho
        self.__rect = pygame.Rect((self.coordenada.x, self.coordenada.y, int(
            self.tamanho.largura), int(self.tamanho.altura)))

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

    def desenhar(self, display):
        cor = (119, 136, 153)  # cinza
        self.__rect.center = (self.coordenada.x, self.coordenada.y)
        pygame.draw.rect(display, cor, self.__rect)
