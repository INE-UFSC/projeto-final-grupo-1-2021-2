from Movel import Movel
from Coordenada import Coordenada
from Tamanho import Tamanho
from Item import Item
from PontoEntrega import PontoEntrega


class Jogador(Movel):
    def __init__(self, coord:Coordenada):
        super().__init__(coord, Tamanho(40,40), 7)
        self.__item_carregado = None

    @property
    def item_carregado(self)->Item:
        return self.__item_carregado

    @item_carregado.setter
    def item_carregado(self, item):
        self.__item_carregado = item

    def pegarItem(self, item: Item) -> bool:
        if(item.ativo and self.coord.calculaDistancia(item.coord) <= item.raio_interacao):
            self.__item_carregado = item
            item.ativo = False
            return True
        else:
            return False

    def perderItem(self):
        self.__item_carregado.ativo = True
        self.__item_carregado = None

    def entregarItem(self, ponto_entrega: PontoEntrega) -> bool:
        if(self.item_carregado != None and self.coord.calculaDistancia(ponto_entrega.coord) <= ponto_entrega.raio_interacao):
            self.item_carregado = None
            return True
        else:
            return False

    def colidiu(self, coord: Coordenada):
        self.atingido = 30
        self.coord_atingido = coord
        if self.item_carregado != None:
            self.perderItem()
        # expandir depois

    def decideDirecao(self, cima: bool, baixo: bool, direita: bool, esquerda: bool):
        if self.atingido == 0:
            horizontal = 0
            vertical = 0
            if(cima):
                vertical -= 1
            if(baixo):
                vertical += 1
            if(direita):
                horizontal += 1
            if(esquerda):
                horizontal -= 1

            self.direcao_deslocamento = Coordenada.versorEntreCoordenadas(
                Coordenada(0, 0), Coordenada(horizontal, vertical))

        else:
            self.direcao_deslocamento = Coordenada.versorEntreCoordenadas(self.coord_atingido, self.coord)
            

    def desenhar(self, display, posicao_camera):
        cor = (0, 0, 255)  # azul
        return super().desenhar(display, cor, posicao_camera)
