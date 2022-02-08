from Biblioteca import Biblioteca
from Item import Item
from Mapa import Mapa
from Fase import Fase
from Jogador import Jogador
from random import randrange
from InimigoObstaculo import InimigoObstaculo
from InimigoPessoa import InimigoPessoa
from PontoEntrega import PontoEntrega


class ConstrutorFase:
    '''def __init__(self, dificuldade : int, mapa : Mapa, lista_itens : list, num_inimigos : int, num_itens : int, nivel : int):
        self.__dificuldade = dificuldade
        self.__mapa = mapa
        self.__lista_itens = lista_itens
        self.__num_inimigos = num_inimigos
        self.__num_itens = num_itens
        self.__nivel = nivel

    #GETTERS
    @property
    def dificuldade(self):
        return self.__dificuldade
    @property
    def mapa(self):
        return self.__mapa
    @property
    def lista_itens(self):
        return self.__lista_itens
    @property
    def num_inimigos(self):
        return self.__num_inimigos
    @property
    def num_itens(self):
        return self.__num_itens
    @property
    def nivel(self):
        return self.__nivel'''

    #METODO
    @staticmethod
    def constroiFase(nivel:str, dificuldade:int) -> Fase:
        mapa = Biblioteca().getMapaNivel(nivel)
        lista_itens = Biblioteca().getItensDificuldade(dificuldade)
        jogador = Jogador(mapa.spawn_jogador)

        num_inimigos = 1 + 2*dificuldade
        inimigos_pessoa, inimigos_obstaculo = [],[]
        for i in range(num_inimigos):
            inimigos_pessoa.append(InimigoPessoa(mapa.spawn_inimigos_p.pop(randrange(len(mapa.spawn_inimigos_p))))) #adiciona um inimigo de um spawn aleatorio
            inimigos_obstaculo.append(InimigoObstaculo(mapa.caminho_inimigos_o.pop(randrange(len(mapa.caminho_inimigos_o)))))

        num_pontos_entrega = 1 if( nivel == 'teste' or nivel == 'mercado') else 1 + 2*dificuldade
        pontos_entrega = []
        for i in range(num_pontos_entrega): #ver esse numero depois
            pontos_entrega.append(PontoEntrega(mapa.pontos_entrega.pop(randrange(len(mapa.pontos_entrega)))))


        return Fase(jogador, inimigos_pessoa, inimigos_obstaculo, mapa, pontos_entrega, lista_itens)
