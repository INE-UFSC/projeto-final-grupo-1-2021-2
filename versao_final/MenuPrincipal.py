import pygame
from pygame.locals import *
from Menu import Menu

class MenuPrincipal(Menu):
    def __init__(self):
        self.altura_jogar = self.altura/2
        self.altura_tutorial = self.altura/2 + 40
        self.altura_creditos = self.altura/2 + 80
        self.altura_sair = self.altura/2 + 120

    def display_menu(self): 
        self.desenha_texto('Nome do Jogo', 40, self.largura / 2,
                           self.altura / 8, self.__branco, self.__fonte)
        self.desenha_texto("  Menu Principal ", 25, self.largura / 2,
                           self.altura / 4, self.__branco, self.__fonte)
        self.desenha_texto("Jogar", 20, self.largura/2,
                           self.altura_jogar, self.__branco, self.__fonte)
        self.desenha_texto("Tutorial", 20, self.largura/2,
                           self.altura_tutorial, self.__branco, self.__fonte)
        self.desenha_texto("Créditos", 20, self.largura/2,
                           self.altura_creditos, self.__branco, self.__fonte)
        self.desenha_texto("Sair", 20, self.largura/2,
                           self.altura_sair, self.__branco, self.__fonte)
        self.desenha_texto("Voltar: A", 20, self.largura/2 - 200,
                           self.altura/2 + 190, self.__branco, self.__fonte)
        self.desenha_texto("Avançar: D", 20, self.largura/2 + 200,
                           self.altura/2 + 190, self.__branco, self.__fonte)
        self.desenha_texto('▶', 20, self.cursor_rect.x,
                           self.cursor_rect.y, self.__branco, self.__fonte)
