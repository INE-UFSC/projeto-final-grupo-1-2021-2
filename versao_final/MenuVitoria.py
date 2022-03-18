import pygame
from pygame.locals import *
from Menu import Menu
from GerenciadorImagens import GerenciadorImagens

class MenuVitoria(Menu):
    def __init__(self, tamanho, ultima_fase:bool):
        super().__init__(tamanho)

        self.__ultima_fase = ultima_fase # mostra ou nao o botao para proxima fase
        
        self.__distancia_cursor = self.largura/2 - 150
        self.__cursor_rect = pygame.Rect(
            self.__distancia_cursor, self.__altura_jogar, 130, 130)
        self.__altura_continuar = self.altura/2 - 120
        self.__altura_menu = self.altura/2 - 60

    def display_menu(self):
        self.display.fill((0, 0, 0))
        self.display.blit(self.fundo, (0, 0))
        self.desenha_texto('Vitória', 60, self.largura / 2,
                           self.altura / 8, self.branco, self.fonte)
        
        if not self.__ultima_fase:
            self.desenha_texto("Próxima fase", 30, self.largura/2,
                           self.__altura_continuar, self.branco, self.fonte)
        self.desenha_texto("Menu princiapal", 30, self.largura/2,
                           self.__altura_menu, self.branco, self.fonte)

        self.desenha_texto("Voltar: Backspace", 20, self.largura/2 - 200,
                           self.altura/2 + 190, self.branco, self.fonte)
        self.desenha_texto("Avançar: Enter", 20, self.largura/2 + 200,
                           self.altura/2 + 190, self.branco, self.fonte)
        self.desenha_texto('▶', 20, self.__cursor_rect.x,
                           self.__cursor_rect.y, self.branco, self.fonte)