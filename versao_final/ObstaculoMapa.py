from Coordenada import Coordenada
from Tamanho import Tamanho
import pygame
from GerenciadorImagens import GerenciadorImagens


class ObstaculoMapa:
    def __init__(self, coordenada: Coordenada = '', tamanho: Tamanho = '', tipo: str = 'balcao_vertical'):
        self.__coord = coordenada
        self.__tamanho = tamanho
        self.__imagem = GerenciadorImagens().getSprite(
            'obstaculo', tipo, tamanho.largura, tamanho.altura)
        # self.__rect = pygame.Rect((self.coord.x, self.coord.y, int(
        # self.tamanho.largura), int(self.tamanho.altura)))
        self.__rect = self.__imagem.get_rect()
        self.__rect.topleft = (self.coord.x, self.coord.y)

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
        # cor = (47, 79, 79)  # cinza escuro
        rect_camera = self.__rect.move(-posicao_camera.x, -posicao_camera.y)
        #pygame.draw.rect(display, cor, rect_camera)
        return self.__imagem, rect_camera
