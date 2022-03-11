import pygame
from Movel import Movel
from Coordenada import Coordenada
from Tamanho import Tamanho


class InimigoPessoa(Movel):
    def __init__(self, spawn: Coordenada, raio_deslocamento: float = 20, raio_deteccao: float = 300, velocidade: float = 3):
        super().__init__(Coordenada(spawn.x, spawn.y), Tamanho(40, 40), velocidade)
        self.__spawn = spawn
        self.__raio_deslocamento = raio_deslocamento
        self.__raio_deteccao = raio_deteccao
        # eh para ser atualizado pelo codigo, talvez mudar isso depois

    def decideDirecao(self, coord_jogador:Coordenada):  # praticamente um versor da direcao de deslocamento
        if self.atingido == 0:
            if(coord_jogador != None and self.coord.calculaDistancia(coord_jogador) <= self.__raio_deteccao):
                self.direcao_deslocamento = Coordenada.versorEntreCoordenadas(
                    self.coord, coord_jogador)
            elif(self.coord.calculaDistancia(self.__spawn) > self.__raio_deslocamento):
                self.direcao_deslocamento = Coordenada.versorEntreCoordenadas(
                    self.coord, self.__spawn)
            else:
                # talvez implementar alguma caminhada aleatoria depois
                self.direcao_deslocamento = Coordenada(0, 0)

        else:
            self.direcao_deslocamento = Coordenada.versorEntreCoordenadas(
                self.coord_atingido, self.coord)

    def colidiu(self, coord: Coordenada):
        # decicir o que fazer (voltar para spawn, ser jogado para tras, ...)
        self.atingido = 30
        self.coord_atingido = coord
        #self.coord = Coordenada(self.__spawn.x, self.__spawn.y)

    def desenhar(self, display, posicao_camera):
        cor = (255, 0, 0)  # vermelho
        return super().desenhar(display, cor, posicao_camera)
