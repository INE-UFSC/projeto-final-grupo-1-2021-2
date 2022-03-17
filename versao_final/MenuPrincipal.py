from select import select
import pygame
from pygame.locals import *
from Menu import Menu
from GerenciadorImagens import GerenciadorImagens


class MenuPrincipal(Menu):
    def __init__(self, tamanho):
        super().__init__(tamanho)
        self.__distancia_cursor = self.largura/2 - 150
        self.__altura_jogar = self.altura/2 - 120
        self.__altura_tutorial = self.altura/2 - 60
        self.__altura_creditos = self.altura/2
        self.__altura_sair = self.altura/2 + 60
        self.__cursor_rect = pygame.Rect(
            self.__distancia_cursor, self.__altura_jogar, 130, 130)

    @property
    def distancia_cursor(self):
        return self.__distancia_cursor

    @property
    def altura_jogar(self):
        return self.__altura_jogar

    @property
    def altura_tutorial(self):
        return self.__altura_tutorial

    @property
    def altura_creditos(self):
        return self.__altura_creditos

    @property
    def altura_sair(self):
        return self.__altura_sair

    @property
    def cursor_rect(self):
        return self.__cursor_rect

    def display_menu(self):
        self.display.fill((0, 0, 0))
        self.display.blit(self.fundo, (0, 0))
        self.desenha_texto('Nome do Jogo', 60, self.largura / 2,
                           self.altura / 8, self.branco, self.fonte)
        self.desenha_texto("  Menu Principal ", 40, self.largura / 2,
                           self.altura / 4, self.branco, self.fonte)
        self.desenha_texto("Jogar", 30, self.largura/2,
                           self.altura_jogar, self.branco, self.fonte)
        self.desenha_texto("Tutorial", 30, self.largura/2,
                           self.altura_tutorial, self.branco, self.fonte)
        self.desenha_texto("Créditos", 30, self.largura/2,
                           self.altura_creditos, self.branco, self.fonte)
        self.desenha_texto("Sair", 30, self.largura/2,
                           self.altura_sair, self.branco, self.fonte)
        self.desenha_texto("Voltar: Backspace", 20, self.largura/2 - 200,
                           self.altura/2 + 190, self.branco, self.fonte)
        self.desenha_texto("Avançar: Enter", 20, self.largura/2 + 200,
                           self.altura/2 + 190, self.branco, self.fonte)
        self.desenha_texto('▶', 20, self.cursor_rect.x,
                           self.cursor_rect.y, self.branco, self.fonte)
