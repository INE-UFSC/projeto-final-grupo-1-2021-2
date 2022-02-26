from Coordenada import Coordenada
from Tamanho import Tamanho
from random import randrange
from ObstaculoMapa import ObstaculoMapa
from PontoEntrega import PontoEntrega
import pygame


class Mapa:
    def __init__(self, tamanho: Tamanho, spawn_jogador: Coordenada, spawn_inimigos_p: list,
                 caminhos_inimigos_o: list, spawn_itens: list,
                 pontos_entrega: list, obstaculos: list):
        self.__tamanho = tamanho
        self.__spawn_jogador = spawn_jogador
        self.__spawn_inimigos_p = spawn_inimigos_p
        self.__caminho_inimigos_o = caminhos_inimigos_o
        self.__spawn_itens = spawn_itens
        self.__pontos_entrega = pontos_entrega
        self.__obstaculos = obstaculos
        self.__rect = pygame.Rect(
            0, 0, self.__tamanho.largura, self.__tamanho.altura)

    # getters

    @property
    def tamanho(self):
        return self.__tamanho

    @property
    def spawn_jogador(self):
        return self.__spawn_jogador

    @property
    def spawn_inimigos_p(self):
        return self.__spawn_inimigos_p

    @property
    def caminho_inimigos_o(self):
        return self.__caminho_inimigos_o

    @property
    def obstaculos(self):
        return self.__obstaculos

    @property
    def pontos_entrega(self) -> PontoEntrega:
        return self.__pontos_entrega

    # métodos

    def coordItemAleatoria(self):
        n = randrange(len(self.__spawn_itens))
        return self.__spawn_itens[n]

    def coordEntregaAleatoria(self):
        n = randrange(len(self.__pontos_entrega))
        return self.__pontos_entrega[n]

    def desenhar(self, display):
        cor = (112, 128, 144)  # cinza
        pygame.draw.rect(display, cor, self.__rect)
        for obstaculo in self.__obstaculos:
            obstaculo.desenhar(display)
