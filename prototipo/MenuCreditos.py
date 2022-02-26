import pygame
from pygame.locals import *
from Menu import Menu

class MenuCreditos(Menu):
    def __init__(self):
        pass

    def display_menu(self, largura, altura):
        fonte = "freesansbold.ttf"
        Menu.desenha_texto('Créditos', 20, largura / 2, altura/ 4 - 20, (255, 255, 255), fonte)
        Menu.desenha_texto('Arthur Torres de Lino', 15, largura / 2, altura / 2 + 10, (255, 255, 255),fonte)
        Menu.desenha_texto('Brenda Silva Machado', 15, largura/ 2, altura/ 2 + 50, fonte)
        Menu.desenha_texto('Gabriela Furtado da Silveira', 15, largura/ 2, altura / 2 + 90, fonte)
        Menu.desenha_texto("Voltar: ←", 10, largura/2 - 200, altura/2 + 190, (255, 255, 255), fonte)
        Menu.desenha_texto("Avançar: →", 10, largura/2 + 200, altura/2 + 190, (255, 255, 255), fonte)