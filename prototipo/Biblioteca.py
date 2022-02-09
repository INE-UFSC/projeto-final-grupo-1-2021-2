from ast import Str
from Mapa import Mapa
from Item import Item
from Coordenada import Coordenada
from ObstaculoMapa import ObstaculoMapa
from Tamanho import Tamanho


class Biblioteca:
    mapas = {
            #mapa para testes
            'teste':Mapa(Tamanho(600,600), Coordenada(100,500), [Coordenada(500,300)], 
            [[Coordenada(240,150),Coordenada(240,450),Coordenada(360,450),Coordenada(360, 150)]],
            [Coordenada(500,100), Coordenada(100,100)], [Coordenada(50,550)], [ObstaculoMapa(Coordenada(290, 200),Tamanho(200, 20))]),
            #mapa mercado
            'mercado':None,
            #mapa cozinha
            'cozinha':None,
            #mapa restaurante
            'restaurante':None
            }
    lista_itens = [
        {'teste':[Item('item1'),Item('item2')]},#itens dificuldade teste (0)
        {'mercado':[], 'cozinha':[], 'restaurante':[]},
        {'mercado':[], 'cozinha':[], 'restaurante':[]},
        {'mercado':[], 'cozinha':[], 'restaurante':[]}
        ]

    @classmethod
    def getMapaNivel(cls, nivel:str)->Mapa:
        return cls.mapas[nivel]

    @classmethod
    def getItensDificuldade(cls, dificuldade:int, nivel:str):
        return cls.lista_itens[dificuldade][nivel]
