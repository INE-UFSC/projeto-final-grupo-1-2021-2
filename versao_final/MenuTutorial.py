import pygame
from pygame.locals import *
from Menu import Menu

class MenuTutorial(Menu):
    def __init__(self):
        self.__fonte = 'PressStart2P-vaV7.ttf'
        self.__branco = ((255, 255, 255))
        self.tamanho_display = self.largura, self.altura = 720*2, 480*2
        self.__display = pygame.display.set_mode(
            self.tamanho_display, pygame.HWSURFACE)
    
    def desenha_texto(self, texto, tamanho, x, y, cor, fonte):
        font = pygame.font.Font(fonte, tamanho)
        text_surface = font.render(texto, True, cor)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.__display.blit(text_surface, text_rect)
           
    def display_menu(self):
        self.__display.fill((0, 0, 0))
        self.desenha_texto('Tutorial', 40, self.largura / 2,
                           self.altura / 2 - 120, self.__branco, self.__fonte)
        self.desenha_texto("Andar para Direira:  D", 15, self.largura/2,
                           self.altura/2 - 30, self.__branco, self.__fonte)
        self.desenha_texto("Andar para Esquerda: A", 15, self.largura/2,
                           self.altura/2, self.__branco, self.__fonte)
        self.desenha_texto("Andar para Cima: W", 15, self.largura/2,
                           self.altura/2 + 30, self.__branco, self.__fonte)
        self.desenha_texto("Andar para Baixo: S", 15, self.largura/2,
                           self.altura/2 + 60, self.__branco, self.__fonte)
        self.desenha_texto("Pegar Item: Espaço", 15, self.largura/2,
                           self.altura/2 + 90, self.__branco, self.__fonte)
        self.desenha_texto("Entregar Item: Espaço", 15, self.largura/2,
                           self.altura/2 + 120, self.__branco, self.__fonte)
        self.desenha_texto("Pausa: Esc", 15, self.largura/2,
                           self.altura/2 + 150, self.__branco, self.__fonte)                   
        self.desenha_texto("Voltar: Backspace", 10, self.largura/2 - 200,
                           self.altura/2 + 190, self.__branco, self.__fonte)
        self.desenha_texto("Avançar: Enter", 10, self.largura/2 + 200,
                           self.altura/2 + 190, self.__branco, self.__fonte)
