from Coordenada import Coordenada
from Tamanho import Tamanho
from random import randrange
from ObstaculoMapa import ObstaculoMapa
from PontoEntrega import PontoEntrega


class Mapa:
    def __init__(self, tamanho: Tamanho, spawn_jogador: Coordenada, spawn_inimigos_p: list[Coordenada],
                 caminhos_inimigos_o: list[list[Coordenada]], spawn_itens: list[Coordenada],
                 pontos_entrega: list[Coordenada], obstaculos: list[ObstaculoMapa]):
        self.__tamanho = tamanho
        self.__spawn_jogador = spawn_jogador
        self.__spawn_inimigos_p = spawn_inimigos_p
        self.__caminho_inimigos_o = caminhos_inimigos_o
        self.__spawn_itens = spawn_itens
        self.__pontos_entrega = pontos_entrega
        self.__obstaculos = obstaculos

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
    def pontos_entrega(self)->PontoEntrega:
        return self.__pontos_entrega

    # métodos

    def coordItemAleatoria(self):
        n = randrange(len(self.__spawn_itens))
        return self.__spawn_itens[n]

    def coordEntregaAleatoria(self):
        n = randrange(len(self.__pontos_entrega))
        return self.__pontos_entrega[n]
