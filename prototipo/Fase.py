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

    def colisao_moveis(self):
        num_moveis = len((self.__jogador, *self.__inimigos_pessoa, *self.__inimigos_obstaculo))
        lista_moveis = [self.__jogador, *self.__inimigos_pessoa, *self.__inimigos_obstaculo]
        for i in range(num_moveis):
            movel_i = lista_moveis[i]
            if i+1 < num_moveis:
                for j in range(i+1, num_moveis):
                    movel_j = lista_moveis[j]
                    if movel_i.rect.colliderect(movel_j.rect):
                        movel_i.colidiu(movel_j.coord)
                        movel_j.colidiu(movel_i.coord)
        
        '''for inim in (*self.inimigos_pessoa, *self.inimigos_obstaculo):
            if self.fase.jogador.rect.colliderect(inim.rect) and self.__teclas_pressionadas['w'] == True:
                # se ele for para cima e colidir, ele volta para trás
                self.fase.jogador.coord.y -= 1
                inim.coord.y += 1
            elif self.fase.jogador.rect.colliderect(inim.rect) and self.__teclas_pressionadas['s'] == True:
                # se ele for para baixo e colidir, ele volta para cima
                self.fase.jogador.coord.y += 1
                inim.coord.y -= 1
            elif self.fase.jogador.rect.colliderect(inim.rect) and self.__teclas_pressionadas['d'] == True:
                # se ele for para direita e colidir, ele volta para esquerda
                self.fase.jogador.coord.x -= 1
                inim.coord.x += 1
            elif self.fase.jogador.rect.colliderect(inim.rect) and self.__teclas_pressionadas['a'] == True:
                # se ele for para esquerda e colidir, ele volta para direita
                self.fase.jogador.coord.x += 1
                inim.coord.x -= 1'''