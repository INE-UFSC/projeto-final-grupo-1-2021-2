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

    @abstractmethod
    # define self.__direcao_deslocamento com base no estado (comando do jogador ou decisao de IA)
    def decideDirecao(self):
        pass

    @abstractmethod
    # define o que acontece quando o objeto colide com outro objeto (na coordenada coord)
    def colidiu(coord: Coordenada):
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

    @coord.setter
    def coord(self, coord: Coordenada):
        self.__coord = coord

    @tamanho.setter
    def tamanho(self, tamanho: Tamanho):
        self.__tamanho = tamanho

    @velocidade.setter
    def velocidade(self, velocidade: float):
        self.__velocidade = velocidade

    def desenhar(self, display, cor):
        pygame.draw.rect(display, cor, (self.coord.x, self.coord.y, int(
            self.tamanho.altura), int(self.tamanho.largura)))
