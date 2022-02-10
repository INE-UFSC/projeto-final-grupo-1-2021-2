from Jogador import Jogador
from Item import Item
from InimigoObstaculo import InimigoObstaculo
from InimigoPessoa import InimigoPessoa
from PontoEntrega import PontoEntrega
from Movel import Movel
from ObstaculoMapa import ObstaculoMapa
from Mapa import Mapa


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
        # self.proximoItem()
        #self.__num_itens = num_itens
        #self.__num_inimigos = num_inimigos

    # GETTERS
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
    def pontos_entrega(self):
        return self.__pontos_entrega

    # METODOS

    def statusJogador(jogador: Jogador):
        pass

    def informacaoCoordenadaJogador(inimigos_pessoa: InimigoPessoa):
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
            if (mov.rect.left+mov.direcao_deslocamento.x < 0 or mov.rect.top+mov.direcao_deslocamento.y < 0
                    or mov.rect.bottom+mov.direcao_deslocamento.y > self.mapa.tamanho.altura or mov.rect.right
                    + mov.direcao_deslocamento.x > self.mapa.tamanho.largura):
                return
            mov.mover(mov.direcao_deslocamento)

    def verificaColisao(movel1: Movel, movel2: Movel):
        pass

    def proximoItem(self) -> bool:
        if len(self.lista_itens) > 0:
            self.__item_ativo = self.__lista_itens.pop(
                0).criar(self.mapa.coordItemAleatoria())
            if len(self.pontos_entrega) == 1:
                self.__ponto_entrega_ativo = self.pontos_entrega[0]
            else:
                self.__ponto_entrega_ativo = self.__pontos_entrega.pop(
                    0).ativar()
            return
        self.__item_ativo = None
        self.__ponto_entrega_ativo = None
        return False
