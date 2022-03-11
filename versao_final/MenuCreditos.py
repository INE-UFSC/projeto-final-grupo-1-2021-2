import pygame
from pygame.locals import *
from Menu import Menu

class MenuCreditos(Menu):
    def __init__(self):
        pass

    def display_menu(self):
        self.__display.fill((0, 0, 0))
        self.desenha_texto('Créditos', 20, self.largura / 2,
                           self.altura / 4 - 20, self.__branco, self.__fonte)
        self.desenha_texto('Arthur Torres de Lino', 15, self.largura / 2,
                           self.altura / 2 + 10, self.__branco, self.__fonte)
        self.desenha_texto('Brenda Silva Machado', 15, self.largura / 2,
                           self.altura / 2 + 50, self.__branco, self.__fonte)
        self.desenha_texto('Gabriela Furtado da Silveira', 15, self.largura /
                           2, self.altura / 2 + 90, self.__branco, self.__fonte)
        self.desenha_texto("Voltar: A", 10, self.largura/2 - 200,
                           self.altura/2 + 190, self.__branco, self.__fonte)
        self.desenha_texto("Avançar: D", 10, self.largura/2 + 200,
                           self.altura/2 + 190, self.__branco, self.__fonte)
