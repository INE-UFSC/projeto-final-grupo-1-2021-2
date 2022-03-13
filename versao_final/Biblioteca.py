from Mapa import Mapa
from Item import Item
from Coordenada import Coordenada
from ObstaculoMapa import ObstaculoMapa
from Tamanho import Tamanho
from Singleton import Singleton


class Biblioteca(metaclass=Singleton):

    def __init__(self):
        self.__mapas = {
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
                    ObstaculoMapa(Coordenada(0, 0), Tamanho(2400, 80), 'balcao_G_vazio'),
                    ObstaculoMapa(Coordenada(0, 80), Tamanho(80, 1400), 'prateleira_garrafas'),
                    ObstaculoMapa(Coordenada(80, 1400), Tamanho(80, 320), 'balcao_P_frutas'),
                    ObstaculoMapa(Coordenada(440, 320), Tamanho(120, 400), 'prateleira_caixas'),
                    ObstaculoMapa(Coordenada(440, 1000), Tamanho(120, 400), 'prateleira_garrafas'),
                    ObstaculoMapa(Coordenada(280, 1640), Tamanho(2120, 80), 'balcao_G_vazio'),
                    ObstaculoMapa(Coordenada(800, 320), Tamanho(120, 400), 'freezer_fechado'),
                    ObstaculoMapa(Coordenada(800, 1000), Tamanho(120, 400), 'balcao_P_verduras'),
                    ObstaculoMapa(Coordenada(1160, 200), Tamanho(120, 240), 'balcao_P_verduras'),
                    ObstaculoMapa(Coordenada(1160, 600), Tamanho(120, 520), 'freezer_pacotes'),
                    ObstaculoMapa(Coordenada(1160, 1280), Tamanho(120, 240), 'prateleira_caixas'),
                    ObstaculoMapa(Coordenada(1520, 240), Tamanho(560, 120), 'balcao_G_verduras'),
                    ObstaculoMapa(Coordenada(1520, 600), Tamanho(560, 120), 'balcao_G_vazio'),
                    ObstaculoMapa(Coordenada(1520, 1000), Tamanho(560, 120), 'prateleira_vazia'),
                    ObstaculoMapa(Coordenada(1520, 1360), Tamanho(560, 120), 'balcao_P_frutas'),
                    ObstaculoMapa(Coordenada(2320, 80), Tamanho(80, 1560), 'freezer_fechado'),
                ], 'mercado'),
            # mapa cozinha
            'cozinha': Mapa(
                #tamanho
                Tamanho(2400, 1720),
                #spawn jogador
                Coordenada(1200, 185),
                #spawn inimigos p
                [
                    Coordenada(185, 465), Coordenada(225, 1495), Coordenada(905, 640), Coordenada(1200, 345),
                    Coordenada(1200, 1225), Coordenada(1465, 640), Coordenada(2215, 465), Coordenada(2175, 1495)
                ],
                #caminhos inimigos o
                [
                    [Coordenada(500, 500), Coordenada(500, 780), Coordenada(1060, 780), Coordenada(1060, 500)],
                    [Coordenada(560, 1060), Coordenada(560, 1180), Coordenada(1120, 1180), Coordenada(1120, 1060)],
                    [Coordenada(480, 1460), Coordenada(480, 1580), Coordenada(1040, 1580), Coordenada(1040, 1460)],
                    [Coordenada(1340, 500), Coordenada(1340, 780), Coordenada(1900, 780), Coordenada(1900, 500)],
                    [Coordenada(1280, 1060), Coordenada(1280, 1180), Coordenada(1840, 1180), Coordenada(1840, 1060)],
                    [Coordenada(1360, 1460), Coordenada(1360, 1580), Coordenada(1920, 1580), Coordenada(1920, 1460)],
                    
                ],
                #spawn itens
                [
                    Coordenada(65, 815), Coordenada(65, 860), Coordenada(65, 905),
                    Coordenada(375, 65), Coordenada(420, 65), Coordenada(465, 65),
                    Coordenada(1935, 65), Coordenada(1980, 65), Coordenada(2025, 65),
                    Coordenada(2335, 815), Coordenada(2335, 860), Coordenada(2335, 905)
                ],
                #pontos entrega
                [
                    Coordenada(330, 550), Coordenada(570, 640), Coordenada(450, 1180), Coordenada(720, 640),
                    Coordenada(840, 1280), Coordenada(1200, 560), Coordenada(1200, 900), Coordenada(1200, 1390),
                    Coordenada(1560, 1280), Coordenada(1670, 640), Coordenada(1780, 320), Coordenada(1840, 640),
                    Coordenada(2080, 1100)
                ],
                #obstaculos
                [
                    ObstaculoMapa(Coordenada(0, 0), Tamanho(2400, 80)),
                    ObstaculoMapa(Coordenada(0, 80), Tamanho(80, 1560)),
                    ObstaculoMapa(Coordenada(80, 760), Tamanho(80, 40)),
                    ObstaculoMapa(Coordenada(80, 920), Tamanho(80, 40)),
                    ObstaculoMapa(Coordenada(0, 1640), Tamanho(2400, 80)),
                    ObstaculoMapa(Coordenada(320, 80), Tamanho(40, 80)),
                    ObstaculoMapa(Coordenada(480, 80), Tamanho(40, 80)),
                    ObstaculoMapa(Coordenada(320, 320), Tamanho(120, 440)),
                    ObstaculoMapa(Coordenada(320, 960), Tamanho(120, 440)),
                    ObstaculoMapa(Coordenada(440, 320), Tamanho(560, 120)),
                    ObstaculoMapa(Coordenada(560, 560), Tamanho(160, 160)),
                    ObstaculoMapa(Coordenada(600, 840), Tamanho(520, 120)),
                    ObstaculoMapa(Coordenada(680, 1280), Tamanho(1040, 120)),
                    ObstaculoMapa(Coordenada(1120, 560), Tamanho(160, 160)),
                    ObstaculoMapa(Coordenada(1280, 840), Tamanho(520, 120)),
                    ObstaculoMapa(Coordenada(1410, 320), Tamanho(560, 120)),
                    ObstaculoMapa(Coordenada(1680, 560), Tamanho(160, 160)),
                    ObstaculoMapa(Coordenada(1880, 80), Tamanho(40, 80)),
                    ObstaculoMapa(Coordenada(2040, 80), Tamanho(40, 80)),
                    ObstaculoMapa(Coordenada(1960, 320), Tamanho(120, 440)),
                    ObstaculoMapa(Coordenada(1960, 960), Tamanho(120, 440)),
                    ObstaculoMapa(Coordenada(2240, 760), Tamanho(80, 40)),
                    ObstaculoMapa(Coordenada(2240, 920), Tamanho(80, 40)),
                    ObstaculoMapa(Coordenada(2320, 80), Tamanho(80, 1560))
                ], 'mercado'),
            # mapa restaurante
            'restaurante': Mapa(
                #tamanho
                Tamanho(2400, 1720),
                #spawn jogador
                Coordenada(1200, 140),
                #spawn inimigos p
                [
                    Coordenada(195, 145), Coordenada(185, 1325), Coordenada(945, 425), Coordenada(945, 815),
                    Coordenada(1205, 225), Coordenada(1765, 625), Coordenada(1765, 1160), Coordenada(1765, 1545)
                ],
                #caminhos inimigos o
                [
                    [Coordenada(535, 160), Coordenada(535, 710), Coordenada(610, 710), Coordenada(610, 160)],
                    [Coordenada(280, 1310), Coordenada(280, 1430), Coordenada(840, 1430), Coordenada(840, 1310)],
                    [Coordenada(1080, 360), Coordenada(1080, 1200), Coordenada(1320, 1200), Coordenada(1320, 360)],
                    [Coordenada(1400, 280), Coordenada(1400, 480), Coordenada(1680, 480), Coordenada(1680, 280)],
                    [Coordenada(1800, 280), Coordenada(1800, 480), Coordenada(2080, 480), Coordenada(2080, 280)],
                    [Coordenada(1480, 830), Coordenada(1480, 1450), Coordenada(2060, 1450), Coordenada(2060, 830)],
                    
                ],
                #spawn itens
                [
                    Coordenada(1055, 1585), Coordenada(1135, 1585), Coordenada(1215, 1585),
                    Coordenada(1295, 1585), Coordenada(1375, 1585)
                ],
                #pontos entrega
                [
                    Coordenada(415, 240), Coordenada(415, 600), Coordenada(735, 240), Coordenada(735, 600),
                    Coordenada(415, 1030), Coordenada(415, 1160), Coordenada(745, 1030), Coordenada(745, 1160),
                    Coordenada(340, 1610), Coordenada(760, 1610), Coordenada(1690, 130), Coordenada(2020, 130),
                    Coordenada(2280, 270), Coordenada(2280, 560), Coordenada(1610, 960), Coordenada(1610, 1320),
                    Coordenada(1930, 960), Coordenada(1930, 1320)
                ],
                #obstaculos
                [
                    ObstaculoMapa(Coordenada(0, 0), Tamanho(2400, 80)),
                    ObstaculoMapa(Coordenada(0, 80), Tamanho(80, 1560)),
                    ObstaculoMapa(Coordenada(0, 1640), Tamanho(2400, 80)),
                    ObstaculoMapa(Coordenada(365, 160), Tamanho(100, 160)),
                    ObstaculoMapa(Coordenada(365, 520), Tamanho(100, 160)),
                    ObstaculoMapa(Coordenada(685, 160), Tamanho(100, 160)),
                    ObstaculoMapa(Coordenada(685, 520), Tamanho(100, 160)),
                    ObstaculoMapa(Coordenada(80, 760), Tamanho(230, 80)),
                    ObstaculoMapa(Coordenada(335, 980), Tamanho(160, 100)),
                    ObstaculoMapa(Coordenada(665, 980), Tamanho(160, 100)),
                    ObstaculoMapa(Coordenada(240, 1080), Tamanho(680, 40)),
                    ObstaculoMapa(Coordenada(335, 1120), Tamanho(160, 100)),
                    ObstaculoMapa(Coordenada(665, 1120), Tamanho(160, 100)),
                    ObstaculoMapa(Coordenada(260, 1560), Tamanho(160, 80)),
                    ObstaculoMapa(Coordenada(680, 1560), Tamanho(160, 80)),
                    ObstaculoMapa(Coordenada(920, 1400), Tamanho(80, 240)),
                    ObstaculoMapa(Coordenada(1000, 1600), Tamanho(400, 40)),
                    ObstaculoMapa(Coordenada(1040, 80), Tamanho(40, 40)),
                    ObstaculoMapa(Coordenada(1080, 80), Tamanho(240, 20)),
                    ObstaculoMapa(Coordenada(1320, 80), Tamanho(40, 40)),
                    ObstaculoMapa(Coordenada(1160, 440), Tamanho(80, 680)),
                    ObstaculoMapa(Coordenada(1610, 80), Tamanho(160, 100)),
                    ObstaculoMapa(Coordenada(1940, 80), Tamanho(160, 100)),
                    ObstaculoMapa(Coordenada(2220, 190), Tamanho(100, 160)),
                    ObstaculoMapa(Coordenada(2220, 480), Tamanho(100, 160)),
                    ObstaculoMapa(Coordenada(2080, 720), Tamanho(240, 80)),
                    ObstaculoMapa(Coordenada(1560, 880), Tamanho(100, 160)),
                    ObstaculoMapa(Coordenada(1880, 880), Tamanho(100, 160)),
                    ObstaculoMapa(Coordenada(1560, 1240), Tamanho(100, 160)),
                    ObstaculoMapa(Coordenada(1880, 1240), Tamanho(100, 160)),
                    ObstaculoMapa(Coordenada(2320, 80), Tamanho(80, 1560))
                ], 'mercado')
        }
        self.__lista_itens = [
            #dificuldade 0
            {'mercado': [Item('Ovo'), Item('Queijo'), Item('Presunto')],
             'cozinha':[Item('Ovo'), Item('Queijo'), Item('Presunto')],
             'restaurante':[Item('Omelete')]},
            #dificuldade 1
            {'mercado': [Item('Massa'), Item('Molho de tomate'), Item('Carne Moida')],
             'cozinha':[Item('Massa'), Item('Molho de tomate'), Item('Carne Moida')],
             'restaurante':[Item('Macarronada'), Item('Lasanha')]},
            #dificuldade 2
            {'mercado': [Item('Arroz'), Item('Feijao'), Item('Carne de porco')],
             'cozinha':[Item('Arroz'), Item('Feijao'), Item('Carne de porco')],
             'restaurante':[Item('Feijoada'), Item('PF')]}
        ]

    def getMapaNivel(self, nivel: str) -> Mapa:
        return self.__mapas[nivel]

    def getItensDificuldade(self, dificuldade: int, nivel: str):
        return [*self.__lista_itens[dificuldade][nivel]]
