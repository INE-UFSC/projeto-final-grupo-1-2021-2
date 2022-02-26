import pygame, sys
from pygame.locals import *
from Menu import Menu

class MenuTutorial(Menu):
    def __init__(self):
        pass
           
    def display_menu(self, display, largura, altura):
        display.fill((0, 0, 0))
        fonte = "freesansbold.ttf"
        self.Menu.desenha_texto('Tutorial', 40, largura/ 2, altura / 2 - 120, (255, 255, 255), fonte)
        self.Menu.desenha_texto("Andar para Direira:  D", 15, largura/2, altura/2 - 30, (255, 255, 255), fonte)
        self.Menu.desenha_texto("Andar para Esquerda: A", 15, largura/2, altura/2, (255, 255, 255), fonte)
        self.Menu.desenha_texto("Andar para Cima: W", 15, largura/2, altura/2 + 30, (255, 255, 255), fonte)
        self.Menu.desenha_texto("Andar para Baixo: S", 15, largura/2, altura/2 + 60, (255, 255, 255), fonte)
        self.Menu.desenha_texto("Pegar Item: Espaço", 15, largura/2, altura/2 + 90, (255, 255, 255), fonte)
        self.Menu.desenha_texto("Entregar Item: Espaço", 15, largura/2, altura/2 + 120, (255, 255, 255), fonte)
        self.Menu.desenha_texto("Voltar: ←", 10, largura/2 - 200, altura/2 + 190, (255, 255, 255), fonte)
        self.Menu.desenha_texto("Avançar: →", 10, largura/2 + 200, altura/2 + 190, (255, 255, 255), fonte)

