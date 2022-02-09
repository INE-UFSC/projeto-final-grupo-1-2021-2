from Coordenada import Coordenada
import pygame


class PontoEntrega:
    def __init__(self, coord: Coordenada, raio_interacao: float = 50):
        self.__coordenada = coord
        self.__raio_interacao = raio_interacao
        self.__rect = pygame.Rect(
            self.__coordenada.x, self.__coordenada.y, 8, 8)

    # getters

    @property
    def coordenada(self):
        return self.__coordenada

    @property
    def raio_interacao(self):
        return self.__raio_interacao

    def desenhar(self, display):
        cor = (34, 139, 34)  # verde escuro
        self.__rect.center = (self.coordenada.x, self.coordenada.y)
        pygame.draw.rect(display, cor, self.__rect)
