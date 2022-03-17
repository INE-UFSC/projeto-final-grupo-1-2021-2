import pygame
from pygame.locals import *
from Menu import Menu
from GerenciadorImagens import GerenciadorImagens

class MenuTutorial(Menu):
    def __init__(self, tamanho):
        #self.fonte = 'PressStart2P-vaV7.ttf'
        #self.branco = ((255, 255, 255))
        #self.tamanho_display = self.largura, self.altura = 720*2, 480*2
        #self.__display = pygame.display.set_mode(
            #self.tamanho_display, pygame.HWSURFACE)
        #self.__fundo = GerenciadorImagens().getSprite(
            #'fundo_menu', 'fundo_menu', self.largura, self.altura)
        super().__init__(tamanho)
    
    #def desenha_texto(self, texto, tamanho, x, y, cor, fonte):
        #font = pygame.font.Font(fonte, tamanho)
        #text_surface = font.render(texto, True, cor)
        #text_rect = text_surface.get_rect()
        #text_rect.center = (x, y)
        #self.__display.blit(text_surface, text_rect)
           
    def display_menu(self):
        self.display.fill((0, 0, 0))
        self.display.blit(self.fundo, (0,0))
        self.desenha_texto('Tutorial', 60, self.largura / 2,
                           self.altura / 8, self.branco, self.fonte)
        self.desenha_texto("Andar para Direira:  D", 25, self.largura/2,
                           self.altura/2 - 190, self.branco, self.fonte)
        self.desenha_texto("Andar para Esquerda: A", 25, self.largura/2,
                           self.altura/2 - 140, self.branco, self.fonte)
        self.desenha_texto("Andar para Cima: W", 25, self.largura/2,
                           self.altura/2 - 90, self.branco, self.fonte)
        self.desenha_texto("Andar para Baixo: S", 25, self.largura/2,
                           self.altura/2 - 40, self.branco, self.fonte)
        self.desenha_texto("Pegar Item: Espaço", 25, self.largura/2,
                           self.altura/2 + 10, self.branco, self.fonte)
        self.desenha_texto("Entregar Item: Espaço", 25, self.largura/2,
                           self.altura/2 + 60, self.branco, self.fonte)
        self.desenha_texto("Pausa: Esc", 25, self.largura/2,
                           self.altura/2 + 110, self.branco, self.fonte)                   
        self.desenha_texto("Voltar: Backspace", 20, self.largura/2 - 200,
                           self.altura/2 + 190, self.branco, self.fonte)
        self.desenha_texto("Avançar: Enter", 20, self.largura/2 + 200,
                           self.altura/2 + 190, self.branco, self.fonte)
