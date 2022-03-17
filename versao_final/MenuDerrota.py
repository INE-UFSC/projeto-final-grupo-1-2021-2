import pygame
from pygame.locals import *
from Menu import Menu
from GerenciadorImagens import GerenciadorImagens

class MenuDerrota(Menu):
    def __init__(self, tamanho):
        super().__init__(tamanho)
        self.distancia_cursor = self.largura/2 - 150
        self.altura_tentar_novamente = self.altura/2 - 120
        self.altura_voltar_menu = self.altura/2 - 60
        self.cursor_rect = pygame.Rect(
            self.distancia_cursor, self.altura_tentar_novamente, 130, 130)

    def display_menu(self):
        self.display.fill((0, 0, 0))
        self.display.blit(self.fundo, (0,0))
        self.desenha_texto("  Você Perdeu ", 40, self.largura / 2,
        self.altura / 4, self.branco, self.fonte)

        self.desenha_texto('Tentar Novamente', 60, self.largura/2,
        self.altura_tentar_novamente, self.branco, self.fonte)

        self.desenha_texto('Menu Principal', 60, self.largura/2,
        self.altura_voltar_menu, self.branco, self.fonte)

        self.desenha_texto('▶', 20, self.cursor_rect.x,
        self.cursor_rect.y, self.branco, self.fonte)

        self.desenha_texto("Avançar: Enter", 20, self.largura/2 + 200,
        self.altura/2 + 190, self.branco, self.fonte)
        self.desenha_texto("Voltar: Backspace", 20, self.largura/2 - 200,
        self.altura/2 + 190, self.branco, self.fonte)