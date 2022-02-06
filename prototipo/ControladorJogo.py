import pygame
from pygame.locals import *
from Fase import Fase

class ControladorJogo:
    def __init__(self):   #, fase : Fase, tempo_restante : int, nivel_atual : int, dificuldade : int):
        self.__rodando = True
        self.__display = None
        self.tamanho_display = self.largura, self.altura = 640, 640
        self.r = 0
        '''
        self.__fase = fase
        self.__tempo_restante = tempo_restante
        self.__nivel_atual = nivel_atual
        self.__dificuldade = dificuldade
        '''

    #GETTERS
    
    @property
    def fase(self):
        return self.__fase
    @property
    def tempo_restante(self):
        return self.__tempo_restante
    @property
    def nivel_atual(self):
        return self.__nivel_atual
    @property
    def dificuldade(self):
        return self.__dificuldade

    #LOOP

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
        self.r = (self.r + 0.01) % 255
        pygame.draw.rect(self.__display, (self.r,0,0), (100,100,100,100), 0)
        pygame.display.flip()

    def limpar(self):
        pygame.quit()

    def executar(self): #def que substitui a execucaoFase
        if self.inicializar() == False:
            self.__rodando = False

        while self.__rodando:
            for evento in pygame.event.get():
                self.eventos(evento)
            self.loop()
            self.renderizar()
        self.limpar()
    
    #CONTROLADOR
    def novaFase(nivel_atual, dificuldade) -> Fase:
        pass
    #VITORIA E DERROTA  


