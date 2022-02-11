from Jogador import Jogador
from Item import Item
from InimigoObstaculo import InimigoObstaculo
from InimigoPessoa import InimigoPessoa
from PontoEntrega import PontoEntrega
from Movel import Movel
from ObstaculoMapa import ObstaculoMapa
from Mapa import Mapa
from random import randrange


class Fase:

    def __init__(self, jogador: Jogador, inimigos_pessoa: list, inimigos_obstaculo: list, mapa: Mapa, pontos_entrega: list, lista_itens: list):
        self.__jogador = jogador
        self.__inimigos_pessoa = inimigos_pessoa
        self.__inimigos_obstaculo = inimigos_obstaculo

        self.__mapa = mapa
        self.__lista_itens = lista_itens
        self.__pontos_entrega = pontos_entrega

        self.__ponto_entrega_ativo = None
        self.__item_ativo = None
        self.proximoItem()
        #self.__num_itens = num_itens
        #self.__num_inimigos = num_inimigos

    # GETTERS
    @property
    def jogador(self):
        return self.__jogador

    @property
    def ponto_entrega_ativo(self)->PontoEntrega:
        return self.__ponto_entrega_ativo

    @property
    def inimigos_obstaculo(self):
        return self.__inimigos_obstaculo

    @property
    def item_ativo(self):
        return self.__item_ativo

    @item_ativo.setter
    def item_ativo(self, item):
        self.__item_ativo = item

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
    def pontos_entrega(self):
        return self.__pontos_entrega

    # METODOS

    def statusJogador(jogador: Jogador):
        pass

    def movimento(self, teclas: dict):
        self.jogador.decideDirecao(
            teclas['w'], teclas['s'], teclas['d'], teclas['a'])

        for inim in self.__inimigos_pessoa:
            inim.coordenada_jogador = self.__jogador.coord
            inim.decideDirecao()

        for inim in self.__inimigos_obstaculo:
            inim.decideDirecao()

        for mov in (*self.__inimigos_pessoa, *self.__inimigos_obstaculo, self.__jogador):
            if (mov.rect.left+mov.direcao_deslocamento.x < 0 or mov.rect.right + mov.direcao_deslocamento.x > self.mapa.tamanho.largura):
                mov.direcao_deslocamento.x = 0
            if(mov.rect.top+mov.direcao_deslocamento.y < 0 or mov.rect.bottom+mov.direcao_deslocamento.y > self.mapa.tamanho.altura):
                mov.direcao_deslocamento.y = 0
            mov.mover(mov.direcao_deslocamento)

    def verificaColisao(movel1: Movel, movel2: Movel):
        pass

    def proximoItem(self) -> bool:
        if len(self.lista_itens) > 0:
            self.__item_ativo = self.__lista_itens.pop(0).criar(self.mapa.coordItemAleatoria())
            self.__ponto_entrega_ativo = self.pontos_entrega[randrange(len(self.pontos_entrega))]
            return False
        self.__item_ativo = None
        self.__ponto_entrega_ativo = None
        return True

    def gerenciamentoItem(self, comando_interagir_item:bool):
        if self.__item_ativo == None and self.__jogador.item_carregado == None:
            if self.proximoItem():
                return True #vitoria
        elif comando_interagir_item and self.__item_ativo != None:
            if self.__jogador.pegarItem(self.__item_ativo):
                pass #acao se pegou

            if self.__jogador.entregarItem(self.ponto_entrega_ativo):
                self.item_ativo = None #acao se entregou
        return False
