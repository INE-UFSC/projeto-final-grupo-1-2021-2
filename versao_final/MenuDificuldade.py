import pygame
from pygame.locals import *
from Menu import Menu
from GerenciadorImagens import GerenciadorImagens

class MenuDificuldade(Menu):
    def __init__(self, tamanho):
        super().__init__(tamanho)
           
    def display_menu(self):
        self.display.fill((0, 0, 0))
        self.display.blit(self.fundo, (0,0))
        self.desenha_texto('Selecionar dificuldade', 60, self.largura / 2,
                           self.altura / 8, self.branco, self.fonte)
        self.desenha_texto("Digite a tecla correspondente:",22, self.largura/2,
                           self.altura/2 - 140, self.branco, self.fonte)
        self.desenha_texto("Fácil: 1", 30, self.largura/2,
                           self.altura/2 - 60, self.branco, self.fonte)
        self.desenha_texto("Médio: 2", 30, self.largura/2,
                           self.altura/2, self.branco, self.fonte)
        self.desenha_texto("Difícil: 3", 30, self.largura/2,
                           self.altura/2 + 60, self.branco, self.fonte)         
        self.desenha_texto("Voltar: Backspace", 20, self.largura/2,
                           self.altura/2 + 190, self.branco, self.fonte)
        
