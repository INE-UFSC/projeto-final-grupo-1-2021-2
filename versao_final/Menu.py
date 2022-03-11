import pygame
from pygame.locals import *

from ControladorJogo import ControladorJogo
from View import View

class Menu(View):
    def __init__(self, controlador : ControladorJogo):
        self.__controlador = controlador
        self.__fonte = 'PressStart2P-vaV7.ttf'
        self.__branco = ((255, 255, 255))
        self.distancia_cursor = self.largura/2 - 100
        self.cursor_rect = pygame.Rect(
            self.distancia_cursor, self.altura/2, 130, 130)

    def desenha_texto(self, texto, tamanho, x, y, cor, fonte):
        font = pygame.font.Font(fonte, tamanho)
        text_surface = font.render(texto, True, cor)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.__display.blit(text_surface, text_rect)


            
