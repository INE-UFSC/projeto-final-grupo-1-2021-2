from typing import Tuple
import pygame, sys
from pygame.locals import *
from GerenciadorImagens import GerenciadorImagens
from abc import abstractmethod, ABC

class Menu(ABC):
    def __init__(self, tamanho: Tuple):
        self.__tamanho_display = self.largura, self.altura = tamanho[0], tamanho[1]
        self.__display = pygame.display.set_mode(
            self.__tamanho_display, pygame.HWSURFACE)
        self.__branco = ((255, 255, 255))
        self.__fonte = 'PressStart2P-vaV7.ttf'
        self.__fundo = GerenciadorImagens().getSprite(
            'fundo_menu', 'fundo_menu', self.largura, self.altura)


    @property
    def tamanho_display(self):
        return self.__tamanho_display
        
    @property
    def display(self):
        return self.__display

    @property
    def branco(self):
        return self.__branco

    @property
    def fonte(self):
        return self.__fonte

    @property
    def fundo(self):
        return self.__fundo

    @fonte.setter
    def fonte(self, fonte):
        self.__fonte = fonte

    @fundo.setter
    def fundo(self, fundo):
        self.__fundo = fundo
        
    def desenha_texto(self, texto, tamanho, x, y, cor, fonte):
        font = pygame.font.Font(fonte, tamanho)
        text_surface = font.render(texto, True, cor)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.__display.blit(text_surface, text_rect) 
    
    @abstractmethod
    def display_menu(self):
        pass
