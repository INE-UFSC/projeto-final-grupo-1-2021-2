from Movel import Movel
from Coordenada import Coordenada
from Tamanho import Tamanho
from copy import deepcopy


class InimigoObstaculo(Movel):
    def __init__(self, caminho:list, tamanho:Tamanho=Tamanho(30,30), velocidade:float=4):
        if(len(caminho) < 2):
            raise ValueError(
                f'Caminho em InimigoObstaculo: {self} eh muito pequeno (len(caminho) < 2)')
        super().__init__(caminho[0], tamanho, velocidade)
        self.__caminho = deepcopy(caminho)
        # adicionar isso no diagrama UML
        self.__proximo_ponto_caminho = 1

    def decideDirecao(self):  # mudar no UML
        if(self.coord.calculaDistancia(self.__caminho[self.__proximo_ponto_caminho]) <= 0.05):
            self.__proximo_ponto_caminho = (
                self.__proximo_ponto_caminho + 1) % len(self.__caminho)
        else:
            direcao = Coordenada.versorEntreCoordenadas(
                self.coord, self.__caminho[self.__proximo_ponto_caminho])
            intensidade_velocidade = (self.coord.calculaDistancia(
                self.__caminho[self.__proximo_ponto_caminho]) / self.velocidade)
            if(intensidade_velocidade >= 1):
                intensidade_velocidade = 1
            self.direcao_deslocamento = Coordenada(
                direcao.x*intensidade_velocidade, direcao.y*intensidade_velocidade)

    def colidiu(coord: Coordenada):  # a principio nao faz nada, talvez implementar algo depois
        pass

    def desenhar(self, display):
        cor = (255, 110, 0)  # laranja
        return super().desenhar(display, cor)
