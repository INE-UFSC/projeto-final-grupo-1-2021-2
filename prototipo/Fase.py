

from Jogador import Jogador
from Item import Item
from InimigoObstaculo import InimigoObstaculo
from InimigoPessoa import InimigoPessoa
from PontoEntrega import PontoEntrega
from Movel import Movel
from ObstaculoMapa import ObstaculoMapa
from Mapa import Mapa

class Fase:

    def __init__(self, jogador : Jogador, inimigos_obstaculo : list, ponto_entrega : PontoEntrega, item : Item, inimigos_pessoa : list,  mapa : Mapa, lista_itens : list, num_itens : int, num_inimigos : int):
        self.__jogador = jogador
        self.__inimigos_obstaculo = inimigos_obstaculo
        self.__item = item
        self.__inimigos_pessoa = inimigos_pessoa
        self.__mapa = mapa
        self.__lista_itens = lista_itens
        self.__num_itens = num_itens
        self.__num_inimigos = num_inimigos
        self.__ponto_entrega = ponto_entrega

    #GETTERS    
    @property
    def jogador(self):
        return self.__jogador
    @property
    def inimigos_obstaculo(self):
        return self.__inimigos_obstaculo
    @property
    def item(self):
        return self.__item
    @property
    def inimigos_pessoa(self):
        return self.__inimigos_pessoa
    @property
    def mapa(self):
        return self.__mapa
    @property
    def lista_itens(self):
        return self.__lista_itens
    @property
    def num_itens(self):
        return self.__num_itens
    @property
    def num_inimigos(self):
        return self.__num_inimigos
    @property
    def ponto_entrega(self):
        return self.__ponto_entrega
    
    #METODOS    

    def statusJogador(jogador : Jogador):
        pass

    def informacaoCoordenadaJogador(inimigos_pessoa : InimigoPessoa):
        pass

    def movimento(movel : Movel, obstaculos: ObstaculoMapa):
        pass

    def verificaColisao(movel1: Movel, movel2: Movel):
        pass

    def proximoItem() -> bool:
        pass
