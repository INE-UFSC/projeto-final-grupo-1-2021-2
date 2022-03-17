from Coordenada import Coordenada
from Interativos import Interativos
import pygame
from GerenciadorImagens import GerenciadorImagens


class Item(Interativos):
    def __init__(self, nome: str):
        self.__nome = nome
        self.__tamanho_lado = 35
        super().__init__(80)
        self.__imagem = GerenciadorImagens().getSprite(
            'item', self.__nome, self.__tamanho_lado, self.__tamanho_lado)

    def criar(self, coordenada: Coordenada):
        self.coord = coordenada
        self.ativo = True
        self.rect = pygame.Rect(
            self.coord.x, self.coord.y, self.__tamanho_lado, self.__tamanho_lado)
        return self

    def desenhar(self, display, posicao_camera):
        cor = (0, 255, 0)  # VERDE
        self.rect.center = (self.coord.x, self.coord.y)
        rect_camera = self.rect.move(-posicao_camera.x, -posicao_camera.y)
        #pygame.draw.rect(display, cor, rect_camera)
        return self.__imagem, rect_camera


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
