from Mapa import Mapa
from Item import Item
from Coordenada import Coordenada
from ObstaculoMapa import ObstaculoMapa
from Tamanho import Tamanho
from Singleton import Singleton


class Biblioteca(metaclass=Singleton):

    def __init__(self):
        self.__mapas = {
            # mapa para testes
            'teste': Mapa(
                #tamanho
                Tamanho(700, 700),
                #spawn jogador
                Coordenada(100, 500),
                #spawn inimigos p
                [
                    Coordenada(500, 300)
                ],
                #caminhos inimigos o
                [
                    [Coordenada(240, 150), Coordenada(240, 450), Coordenada(360, 450), Coordenada(360, 150)]
                ],
                #spawn itens
                [
                    Coordenada(500, 100), Coordenada(100, 100)
                ],
                #pontos entrega
                [
                    Coordenada(50, 550)
                ],
                #obstaculos
                [
                    ObstaculoMapa(Coordenada(290, 200), Tamanho(20, 200))
                ]),
            # mapa mercado
            'mercado': Mapa(
                #tamanho
                Tamanho(2400, 1720),
                #spawn jogador
                Coordenada(220, 1520),
                #spawn inimigos p
                [
                    Coordenada(185, 875), Coordenada(860, 195), Coordenada(860, 875), Coordenada(1405, 875),
                    Coordenada(1800, 165), Coordenada(1800, 485), Coordenada(1800, 1245), Coordenada(1800, 1560)
                ],
                #caminhos inimigos o
                [
                    [Coordenada(320, 920), Coordenada(320, 1460), Coordenada(680, 1460), Coordenada(680, 920)],
                    [Coordenada(320, 260), Coordenada(320, 800), Coordenada(680, 800), Coordenada(680, 260)],
                    [Coordenada(1040, 140), Coordenada(1040, 520), Coordenada(1400, 520), Coordenada(1400, 140)],
                    [Coordenada(1040, 1200), Coordenada(1040, 1580), Coordenada(1400, 1580), Coordenada(1400, 1200)],
                    [Coordenada(1520, 800), Coordenada(1520, 920), Coordenada(2080, 920), Coordenada(2080, 800)],
                    [Coordenada(2160, 160), Coordenada(2160, 1560), Coordenada(2240, 1560), Coordenada(2240, 160)],
                    
                ],
                #spawn itens
                [
                    Coordenada(65, 535), Coordenada(545, 520), Coordenada(455, 1035), Coordenada(905, 1200),
                    Coordenada(1220, 65), Coordenada(1175, 715), Coordenada(1265, 1005), Coordenada(1220, 1295),
                    Coordenada(1220, 1505), Coordenada(1675, 65), Coordenada(1535, 300), Coordenada(2065, 300),
                    Coordenada(1595, 615), Coordenada(1975, 705), Coordenada(1800, 1015), Coordenada(1535, 1415),
                    Coordenada(1935, 1655), Coordenada(2335, 475), Coordenada(2335, 865), Coordenada(2335, 1625)
                ],
                #pontos entrega
                [
                    Coordenada(170, 1520)
                ],
                #obstaculos
                [
                    ObstaculoMapa(Coordenada(0, 0), Tamanho(2400, 80)),
                    ObstaculoMapa(Coordenada(0, 80), Tamanho(80, 1400)),
                    ObstaculoMapa(Coordenada(80, 1400), Tamanho(80, 320)),
                    ObstaculoMapa(Coordenada(440, 320), Tamanho(120, 400)),
                    ObstaculoMapa(Coordenada(440, 1000), Tamanho(120, 400)),
                    ObstaculoMapa(Coordenada(280, 1640), Tamanho(2120, 80)),
                    ObstaculoMapa(Coordenada(800, 320), Tamanho(120, 400)),
                    ObstaculoMapa(Coordenada(800, 1000), Tamanho(120, 400)),
                    ObstaculoMapa(Coordenada(1160, 200), Tamanho(120, 240)),
                    ObstaculoMapa(Coordenada(1160, 600), Tamanho(120, 520)),
                    ObstaculoMapa(Coordenada(1160, 1280), Tamanho(120, 240)),
                    ObstaculoMapa(Coordenada(1520, 240), Tamanho(560, 120)),
                    ObstaculoMapa(Coordenada(1520, 600), Tamanho(560, 120)),
                    ObstaculoMapa(Coordenada(1520, 1000), Tamanho(560, 120)),
                    ObstaculoMapa(Coordenada(1520, 1360), Tamanho(560, 120)),
                    ObstaculoMapa(Coordenada(2320, 80), Tamanho(80, 1560)),
                ]),
            # mapa cozinha
            'cozinha': None,
            # mapa restaurante
            'restaurante': None
        }
        self.__lista_itens = [
            {'teste': [Item('item1'), Item('item2'), Item('item3')]
             },  # itens dificuldade teste (0)
            {'mercado': [Item('item1'), Item('item2'), Item('item3')], 'cozinha':[], 'restaurante':[]},
            {'mercado': [Item('item1'), Item('item2'), Item('item3')], 'cozinha':[], 'restaurante':[]},
            {'mercado': [Item('item1'), Item('item2'), Item('item3')], 'cozinha':[], 'restaurante':[]}
        ]

    def getMapaNivel(self, nivel: str) -> Mapa:
        return self.__mapas[nivel]

    def getItensDificuldade(self, dificuldade: int, nivel: str):
        return self.__lista_itens[dificuldade][nivel]
