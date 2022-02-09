from Jogador import Jogador
from Item import Item
from InimigoObstaculo import InimigoObstaculo
from InimigoPessoa import InimigoPessoa
from PontoEntrega import PontoEntrega
from Movel import Movel
from ObstaculoMapa import ObstaculoMapa
from Mapa import Mapa

class Fase:

    def __init__(self, jogador:Jogador, inimigos_pessoa:list, inimigos_obstaculo:list, mapa:Mapa, pontos_entrega:list, lista_itens:list):
        self.__jogador = jogador
        self.__inimigos_pessoa = inimigos_pessoa
        self.__inimigos_obstaculo = inimigos_obstaculo

        self.__mapa = mapa
        self.__lista_itens = lista_itens
        self.__pontos_entrega = pontos_entrega
        
        self.__item_ativo = None
        self.proximoItem()
        #self.__num_itens = num_itens
        #self.__num_inimigos = num_inimigos

    #GETTERS    
    @property
    def jogador(self):
        return self.__jogador
    @property
    def inimigos_obstaculo(self):
        return self.__inimigos_obstaculo
    @property
    def item_ativo(self):
        return self.__item_ativo
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

    def proximoItem(self) -> bool:
        self.__lista_itens.pop(0).criar(self.mapa.coordItemAleatoria())
