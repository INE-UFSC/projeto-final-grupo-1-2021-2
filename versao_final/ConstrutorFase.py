from Biblioteca import Biblioteca
from Item import Item
from Mapa import Mapa
from Fase import Fase
from Jogador import Jogador
from random import randrange
from InimigoObstaculo import InimigoObstaculo
from InimigoPessoa import InimigoPessoa
from PontoEntrega import PontoEntrega
from Singleton import Singleton
from math import ceil


class ConstrutorFase(metaclass=Singleton):
    def __init__(self):
        self.__biblioteca = Biblioteca()
    '''def __init__(self, dificuldade : int, mapa : Mapa, lista_itens : list, num_inimigos : int, num_itens : int, nivel : int):
        self.__dificuldade = dificuldade
        self.__mapa = mapa
        self.__lista_itens = lista_itens
        self.__num_inimigos = num_inimigos
        self.__num_itens = num_itens
        self.__nivel = nivel

    #GETTERS
    @property
    def dificuldade(self):
        return self.__dificuldade
    @property
    def mapa(self):
        return self.__mapa
    @property
    def lista_itens(self):
        return self.__lista_itens
    @property
    def num_inimigos(self):
        return self.__num_inimigos
    @property
    def num_itens(self):
        return self.__num_itens
    @property
    def nivel(self):
        return self.__nivel'''

    #METODO
    def constroiFase(self, nivel:str, dificuldade:int) -> Fase:
        mapa = self.__biblioteca.getMapaNivel(nivel)

        jogador = Jogador(mapa.spawn_jogador)
        #dificuldade de 1 a 3
        num_inimigos_p = ceil((dificuldade+1)/3 * len(mapa.spawn_inimigos_p))
        num_inimigos_o = ceil((dificuldade+1)/3 * len(mapa.caminho_inimigos_o))

        lista_spawn_p = mapa.spawn_inimigos_p
        lista_caminhos_o = mapa.caminho_inimigos_o
        inimigos_pessoa, inimigos_obstaculo = [],[]
        for i in range(num_inimigos_p):
            inimigos_pessoa.append(InimigoPessoa(lista_spawn_p.pop(randrange(len(lista_spawn_p))))) #adiciona um inimigo de um spawn aleatorio
        for i in range(num_inimigos_o):
            inimigos_obstaculo.append(InimigoObstaculo(lista_caminhos_o.pop(randrange(len(lista_caminhos_o)))))

        pontos_entrega = []
        for pe in mapa.pontos_entrega:
            pontos_entrega.append(PontoEntrega(pe))

        num_itens = 6 + dificuldade * 2
        itens_diferentes = len(self.__biblioteca.getItensDificuldade(dificuldade, nivel))
        lista_itens = []
        for i in range(num_itens):
            lista_itens.append(self.__biblioteca.getItensDificuldade(dificuldade, nivel)[randrange(itens_diferentes)])

        return Fase(jogador, inimigos_pessoa, inimigos_obstaculo, mapa, pontos_entrega, lista_itens)
