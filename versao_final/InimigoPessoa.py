import pygame
from Movel import Movel
from Coordenada import Coordenada
from Tamanho import Tamanho
from GerenciadorImagens import GerenciadorImagens


class InimigoPessoa(Movel):
    def __init__(self, spawn: Coordenada, raio_deslocamento: float = 20, raio_deteccao: float = 300, velocidade: float = 3, sprites: list = []):
        super().__init__(Coordenada(spawn.x, spawn.y), Tamanho(40, 40), velocidade, sprites)
        self.__spawn = spawn
        self.__raio_deslocamento = raio_deslocamento
        self.__raio_deteccao = raio_deteccao
        self.__imagem_atual = None
        # eh para ser atualizado pelo codigo, talvez mudar isso depois

    # praticamente um versor da direcao de deslocamento
    def decideDirecao(self, coord_jogador: Coordenada):
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
        # cor = (255, 0, 0)  # vermelho
        if self.atingido:
            imagem = self.imagens[len(self.imagens)-2]
            if self.angulo >= 180:
                imagem = self.imagens[len(self.imagens)-1]
        elif self.direcao_deslocamento.x == 0 and self.direcao_deslocamento.y == 0:
            if self.angulo < 180:
                imagem = self.imagens[0]
            else:
                imagem = self.imagens[1]
        elif self.direcao_deslocamento.x < 0 or (self.direcao_deslocamento.x == 0 and self.direcao_deslocamento.y < 0):
            if self.__imagem_atual == self.imagens[2]:
                imagem = self.imagens[3]
            else:
                imagem = self.imagens[2]
        else:
            if self.__imagem_atual == self.imagens[4]:
                imagem = self.imagens[5]
            else:
                imagem = self.imagens[4]

        self.__imagem_atual = imagem
        return imagem, super().desenhar(display, posicao_camera)

    def salvar_imagens(self, sprites: list):
        lista = []
        for nome in sprites:
            lista.append(GerenciadorImagens().getSprite(
                'inimigo_pessoa', nome, self.tamanho.largura, self.tamanho.altura))
        return lista
