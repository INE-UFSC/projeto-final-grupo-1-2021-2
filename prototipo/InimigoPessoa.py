from Movel import Movel
from Coordenada import Coordenada
from Tamanho import Tamanho

class InimigoPessoa(Movel):
    def __init__(self, spawn:Coordenada, tamanho:Tamanho, velocidade:float, raio_deslocamento:float, raio_deteccao:float):
        super.__init__(spawn, tamanho, velocidade)
        self.__spawn = spawn
        self.__raio_deslocamento = raio_deslocamento
        self.__raio_deteccao = raio_deteccao
        self.__coordenada_jogador = spawn #eh para ser atualizado pelo codigo, talvez mudar isso depois

    def decideDirecao(self): #praticamente um versor da direcao de deslocamento
        if(self.__coord.calculaDistancia(self.__coordenada_jogador) <= self.__raio_deteccao):
            self.__direcao_deslocamento = Coordenada.versorEntreCoordenadas(self.__coord, self.__coordenada_jogador)
        elif(self.__coord.calculaDistancia(self.__spawn) > self.__raio_deslocamento):
            self.__direcao_deslocamento = Coordenada.versorEntreCoordenadas(self.__coord, self.__spawn)
        else:
            self.__direcao_deslocamento = Coordenada(0,0) #talvez implementar alguma caminhada aleatoria depois

    def colidiu(self, coord:Coordenada):
        pass #decicir o que fazer (voltar para spawn, ser jogado para tras, ...)
