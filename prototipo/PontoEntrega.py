import imp
from Coordenada import Coordenada
from Interativos import Interativos
import pygame


class PontoEntrega(Interativos):
    def __init__(self, coord: Coordenada, raio_interacao: float = 50):
        super().__init__(raio_interacao, coord)
        self.rect = pygame.Rect(self.coord.x, self.coord.y, 50, 50)

    def desenhar(self, display, posicao_camera):
        cor = (34, 139, 34)  # verde escuro
        self.rect.center = (self.coord.x, self.coord.y)
        #self.rect.x = - posicao_camera.x
        #self.rect.y = - posicao_camera.y
        rect_camera = self.rect.move(-posicao_camera.x, -posicao_camera.y)
        pygame.draw.rect(display, cor, rect_camera)

    def ativar(self):
        self.ativo = True
        return self


'''    @property
    def coordenada(self):
        return self.__coordenada

    @property
    def raio_interacao(self):
        return self.__raio_interacao'''
