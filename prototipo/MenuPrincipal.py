
import pygame, sys
from pygame.locals import *
from Menu import Menu

class MenuPrincipal(Menu):
    def __init__(self, display):
        Menu.__init__(self, display)

    def display_menu(self, largura, altura):
        self.cursor_rect = pygame.Rect(0, 0, 130, 130)
        fonte = "freesansbold.ttf"
        self.desenha_texto('Nome do Jogo', 40, largura/ 2, altura / 8, (255, 255, 255), fonte)
        self.__menu.desenha_texto("Menu Principal ", 15, largura / 2, altura / 4, (255, 255, 255), fonte)
        self.__menu.desenha_texto("Jogar", 20, largura/2, altura/2, (255, 255, 255), fonte)
        self.__menu.desenha_texto("Tutorial", 20, largura/2, altura/2 + 40, (255, 255, 255), fonte)
        self.__menu.desenha_texto("Créditos", 20, largura/2, altura/2 + 80, (255, 255, 255), fonte)
        self.__menu.desenha_texto("Sair", 20, largura/2, altura/2 + 120, (255, 255, 255), fonte)
        self.__menu.desenha_texto("Voltar: ←", 10, largura/2 - 200, altura/2 + 190, (255, 255, 255), fonte)
        self.__menu.desenha_texto("Avançar: →", 10, largura/2 + 200, altura/2 + 190, (255, 255, 255), fonte)
        self.__menu.desenha_texto('▶', 20, self.cursor_rect.x, self.cursor_rect.y)
