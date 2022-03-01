import pygame
from Coordenada import Coordenada
from Tamanho import Tamanho
from abc import ABC, abstractmethod


class Movel(ABC):
    def __init__(self, coord: Coordenada, tamanho: Tamanho, velocidade: float):
        self.__coord = coord
        self.__tamanho = tamanho
        self.__velocidade = velocidade
        self.__direcao_deslocamento = Coordenada(0, 0)
        self.__rect = pygame.Rect((self.coord.x, self.coord.y, int(
            self.tamanho.largura), int(self.tamanho.altura)))
        self.__atingido = False
        self.__coord_atingido = None

    @abstractmethod
    # define self.__direcao_deslocamento com base no estado (comando do jogador ou decisao de IA)
    def decideDirecao(self):
        pass

    # define o que acontece quando o objeto colide com outro objeto (na coordenada coord)
    def colidiu(self, coord: Coordenada):
        pass

    @property
    def coord(self) -> Coordenada:
        return self.__coord

    @property
    def tamanho(self) -> Tamanho:
        return self.__tamanho

    @property
    def velocidade(self) -> float:
        return self.__velocidade

    @property
    def direcao_deslocamento(self) -> Coordenada:
        return self.__direcao_deslocamento

    @property
    def rect(self):
        return self.__rect

    @property
    def atingido(self) -> int:
        return self.__atingido

    @property
    def coord_atingido(self) -> Coordenada:
        return self.__coord_atingido

    @coord.setter
    def coord(self, coord: Coordenada):
        self.__coord = coord

    @tamanho.setter
    def tamanho(self, tamanho: Tamanho):
        self.__tamanho = tamanho

    @velocidade.setter
    def velocidade(self, velocidade: float):
        self.__velocidade = velocidade

    @direcao_deslocamento.setter
    def direcao_deslocamento(self, dir: Coordenada):
        self.__direcao_deslocamento = dir

    @atingido.setter
    def atingido(self, atingido: int):
        self.__atingido = atingido

    @coord_atingido.setter
    def coord_atingido(self, coord: Coordenada):
        self.__coord_atingido = Coordenada(coord.x, coord.y)

    def desenhar(self, display, cor, posicao_camera):
        #self.__rect.centerx = self.__coord.x - posicao_camera.x
        #self.__rect.centery = self.__coord.y - posicao_camera.y
        rect_camera = self.__rect.move(-posicao_camera.x, -posicao_camera.y)
        pygame.draw.rect(display, cor, rect_camera)

    def velocidade_real(self) -> float:
        return self.velocidade * 2 if self.atingido > 0 else self.velocidade

    def mover(self):
        if self.atingido > 0:
            self.atingido -= 1
        direcao = self.__direcao_deslocamento
        velocidade = self.velocidade_real()
        self.__coord.mover(direcao.x*velocidade,
                           direcao.y*velocidade)
        self.__rect.center = self.coord.x, self.coord.y


'''    def desenhar(self, display, cor):
        pygame.draw.rect(display, cor, (self.coord.x, self.coord.y, int(
            self.tamanho.largura), int(self.tamanho.altura)))'''
