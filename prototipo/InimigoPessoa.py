import pygame
from Movel import Movel
from Coordenada import Coordenada
from Tamanho import Tamanho


class InimigoPessoa(Movel):
    def __init__(self, spawn:Coordenada, raio_deslocamento:float=20, raio_deteccao:float=200, velocidade:float=2):
        super().__init__(Coordenada(spawn.x, spawn.y), Tamanho(20,20), velocidade)
        self.__spawn = spawn
        self.__raio_deslocamento = raio_deslocamento
        self.__raio_deteccao = raio_deteccao
        self.__coordenada_jogador = None #eh para ser atualizado pelo codigo, talvez mudar isso depois

    def decideDirecao(self): #praticamente um versor da direcao de deslocamento
        if(self.__coordenada_jogador != None and self.coord.calculaDistancia(self.__coordenada_jogador) <= self.__raio_deteccao):
            self.direcao_deslocamento = Coordenada.versorEntreCoordenadas(self.coord, self.__coordenada_jogador)
        elif(self.coord.calculaDistancia(self.__spawn) > self.__raio_deslocamento):
            self.direcao_deslocamento = Coordenada.versorEntreCoordenadas(self.coord, self.__spawn)
        else:
            # talvez implementar alguma caminhada aleatoria depois
            self.direcao_deslocamento = Coordenada(0, 0)

    @property
    def coordenada_jogador(self)->Coordenada:
        return self.__coordenada_jogador
    
    @coordenada_jogador.setter
    def coordenada_jogador(self, coord:Coordenada):
        self.__coordenada_jogador = coord

    def colidiu(self, coord: Coordenada):
        # decicir o que fazer (voltar para spawn, ser jogado para tras, ...)
        self.coord = Coordenada(self.__spawn.x, self.__spawn.y)


    def desenhar(self, display):
        cor = (255, 0, 0) #vermelho
        return super().desenhar(display, cor)
