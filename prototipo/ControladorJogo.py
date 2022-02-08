import pygame
from pygame.locals import *
from Fase import Fase
from ConstrutorFase import ConstrutorFase

class ControladorJogo:
    def __init__(self):   #, fase : Fase, tempo_restante : int, nivel_atual : int, dificuldade : int):
        self.__rodando = True
        self.__display = None
        self.tamanho_display = self.largura, self.altura = 640, 640
        self.__fase = None
        '''
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
        self.novaFase('teste', 0)

    def eventos(self, evento):
        if evento.type == pygame.QUIT:
            self.__rodando = False

    def loop(self):
        pass

    def renderizar(self):
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
    def novaFase(self, nivel_atual:str, dificuldade:float):
        self.__fase = ConstrutorFase.constroiFase(nivel_atual, dificuldade)
    #VITORIA E DERROTA  


