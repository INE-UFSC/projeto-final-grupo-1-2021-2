from Coordenada import Coordenada
from Tamanho import Tamanho
import pygame


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

    def desenhar(self, display):
        cor = (119, 136, 153)  # cinza
        pygame.draw.rect(display, cor, (self.coordenada.x, self.coordenada.y, int(
            self.tamanho.altura), int(self.tamanho.largura)))
