from Movel import Movel
from Coordenada import Coordenada
from Tamanho import Tamanho
from Item import Item
from PontoEntrega import PontoEntrega


class Jogador(Movel):
    def __init__(self, coord:Coordenada):
        super().__init__(coord, Tamanho(20,20), 0.1)
        self.__item_carregado = None

    def pegarItem(self, item: Item) -> bool:
        if(self.__coord.calculaDistancia(item.coord) <= item.raio_interacao):
            self.__item_carregado = item
            item.ativo = False
            return True
        else:
            return False

    def removerItem(self):
        self.__item_carregado = None

    def entregarItem(self, ponto_entrega: PontoEntrega) -> bool:
        if(self.__coord.calculaDistancia(ponto_entrega.coord) <= ponto_entrega.raio_interacao):
            self.removerItem()
            return True
        else:
            return False

    def colidiu(self, coord: Coordenada):
        self.removerItem()
        # expandir depois

    def decideDirecao(self, cima: bool, baixo: bool, direita: bool, esquerda: bool):
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

    def desenhar(self, display):
        cor = (0, 0, 255)  # azul
        return super().desenhar(display, cor)
