import pygame, sys
from pygame.locals import *

class Menu:
    def __init__(self, display):
        self.__display = display       

    def desenha_texto(self, texto, tamanho, x, y, cor, fonte): 
        font = pygame.font.Font(fonte, tamanho)
        text_surface = font.render(texto, True, cor)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.__display.blit(text_surface,text_rect)

            