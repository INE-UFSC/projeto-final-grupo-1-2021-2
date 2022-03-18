from Singleton import Singleton
import pygame
import os


class GerenciadorSons(metaclass=Singleton):
    def __init__(self):
        pygame.mixer.init()
        self.__local_music = {

            'musica': {
                'musica_jogo': 'musica_jogo.mp3',
                'musica_menu': 'musica_menu.mp3' }
            }
        self.__local_sons = {
            'sons': { 
                'apertou_botao': 'apertou_botao.wav',
                'colisao': 'colisao.wav',
                'item': 'item.wav',
                'mudando_cursor': 'mudando_cursor.wav'
            }
        }
        self.__sons_carregados = None
        self.__carregarSons()
        self.__musicas_carregadas = None
        self.__carregarMusicas()

    def __carregarSons(self):
        sons = {}
        for componente, som in self.__local_sons.items():
            sons[componente] = {}
            for descricao, som in som.items():
                sons[componente][descricao] = pygame.mixer.Sound(
                    os.path.join('versao_final', 'sons', som))


        self.__sons_carregados = sons

    def __carregarMusicas(self):
        musicas = {}
        for componente, musica in self.__local_music.items():
            musicas[componente] = {}
            for descricao, musica in musica.items():
                musicas[componente][descricao] = pygame.mixer.music.load(
                    os.path.join('versao_final', 'sons', musica))


        self.__musicas_carregadas = musicas

    def getSound(self, componente: str, descricao: str):
        som = self.__sons_carregados[componente][descricao]
        return som
    
    def getMusic(self, componente: str, descricao: str):
        musica = self.__musicas_carregadas[componente][descricao]
        return musica
