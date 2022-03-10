import pygame
from pygame.locals import *

class View:
    def __init__(self):
        self.__display = None
        self.tamanho_display = self.largura, self.altura = 720*2, 480*2


    def inicializa_display(self):
        self.__display = pygame.display.set_mode(
            self.tamanho_display, pygame.HWSURFACE)
    @property
    def display(self):
        return self.__display