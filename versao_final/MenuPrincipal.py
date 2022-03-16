import pygame
from pygame.locals import *
from Menu import Menu
from GerenciadorImagens import GerenciadorImagens

class MenuPrincipal(Menu):
    def __init__(self):
        self.__fonte = 'PressStart2P-vaV7.ttf'
        self.__branco = ((255, 255, 255))
        self.tamanho_display = self.largura, self.altura = 720*2, 480*2
        self.distancia_cursor = self.largura/2 - 150
        self.__display = pygame.display.set_mode(
            self.tamanho_display, pygame.HWSURFACE)
        self.altura_jogar = self.altura/2 - 120
        self.altura_tutorial = self.altura/2 - 60
        self.altura_creditos = self.altura/2 
        self.altura_sair = self.altura/2 + 60
        self.cursor_rect = pygame.Rect(
            self.distancia_cursor, self.altura_jogar, 130, 130)
        self.__fundo = GerenciadorImagens().getSprite(
            'fundo_menu', 'fundo_menu', self.largura, self.altura)

    def desenha_texto(self, texto, tamanho, x, y, cor, fonte):
        font = pygame.font.Font(fonte, tamanho)
        text_surface = font.render(texto, True, cor)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.__display.blit(text_surface, text_rect)
        

    def display_menu(self): 
        self.__display.fill((0, 0, 0))
        self.__display.blit(self.__fundo, (0,0))
        self.desenha_texto('Nome do Jogo', 60, self.largura / 2,
                           self.altura / 8, self.__branco, self.__fonte)
        self.desenha_texto("  Menu Principal ", 40, self.largura / 2,
                           self.altura / 4, self.__branco, self.__fonte)
        self.desenha_texto("Jogar", 30, self.largura/2,
                           self.altura_jogar, self.__branco, self.__fonte)
        self.desenha_texto("Tutorial", 30, self.largura/2,
                           self.altura_tutorial, self.__branco, self.__fonte)
        self.desenha_texto("Créditos", 30, self.largura/2,
                           self.altura_creditos, self.__branco, self.__fonte)
        self.desenha_texto("Sair", 30, self.largura/2,
                           self.altura_sair, self.__branco, self.__fonte)
        self.desenha_texto("Voltar: Backspace", 20, self.largura/2 - 200,
                           self.altura/2 + 190, self.__branco, self.__fonte)
        self.desenha_texto("Avançar: Enter", 20, self.largura/2 + 200,
                           self.altura/2 + 190, self.__branco, self.__fonte)
        self.desenha_texto('▶', 20, self.cursor_rect.x,
                           self.cursor_rect.y, self.__branco, self.__fonte)
