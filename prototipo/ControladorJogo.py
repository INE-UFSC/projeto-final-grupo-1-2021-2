import pygame
from pygame.locals import *

class ControladorJogo:
    def __init__(self):
        self.__rodando = True
        self.__display = None
        self.tamanho_display = self.largura, self.altura = 640, 400

    def inicializar(self):
        pygame.init()
        self.__display = pygame.display.set_mode(self.tamanho_display, pygame.HWSURFACE)
        self.__rodando = True

    def eventos(self, evento):
        if evento.type == pygame.QUIT:
            self.__rodando = False

    def loop(self):
        pass

    def renderizar(self):
        pass

    def limpar(self):
        pygame.quit()

    def executar(self):
        if self.inicializar() == False:
            self.__rodando = False

        while self.__rodando:
            for evento in pygame.event.get():
                self.eventos(evento)
            self.loop()
            self.renderizar()
        self.limpar()