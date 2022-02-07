from Mapa import Mapa
from Item import Item
from prototipo.Coordenada import Coordenada
from prototipo.ObstaculoMapa import ObstaculoMapa
from prototipo.Tamanho import Tamanho


class Biblioteca:
    mapas = [
            #mapa para testes
            Mapa(Tamanho(600,600), Coordenada(100,500), [Coordenada(500,300)], 
            [[Coordenada(240,150),Coordenada(240,450),Coordenada(360,450),Coordenada(360, 150)]],
            [Coordenada(500,100), Coordenada(100,100)], [Coordenada(50,550)], [ObstaculoMapa(Coordenada(290, 200),Tamanho(200, 20))]),
            #mapa mercado

            #mapa cozinha

            #mapa restaurante
            ]
    lista_itens = [
        {'teste':[Item('item1', 30),Item('item2', 30)]},
        {'mercado':[], 'cozinha':[], 'restaurante':[]},
        {'mercado':[], 'cozinha':[], 'restaurante':[]},
        {'mercado':[], 'cozinha':[], 'restaurante':[]}
        ]

    '''def __init__(self, mapas: list[Mapa], lista_itens: list[dict[list[Item]]]):
        self.__mapas = [
            Mapa(Tamanho(600,600), Coordenada(100,500), [Coordenada(500,300)], #mapa para testes
            [[Coordenada(240,150),Coordenada(240,450),Coordenada(360,450),Coordenada(360, 150)]],
            [Coordenada(500,100), Coordenada(100,100)], [Coordenada(50,550)], [ObstaculoMapa(Coordenada(290, 200),Tamanho(200, 20))])
            ,*mapas]
        self.__lista_itens = [
            {'teste':[Item('item1', 30),Item('item2', 30)]}, *lista_itens]'''

    @classmethod
    def getMapaNivel(cls, nivel):
        return cls.mapas[nivel]

    @classmethod
    def getItensDificuldade(cls, dificuldade):
        return cls.__lista_itens[dificuldade]
