import pygame
from pygame.locals import *
from Fase import Fase
from ConstrutorFase import ConstrutorFase
from InimigoPessoa import InimigoPessoa
from Jogador import Jogador

class ControladorJogo:
    def __init__(self):   #, fase : Fase, tempo_restante : int, nivel_atual : int, dificuldade : int):
        self.__rodando = True
        self.__display = None
        self.tamanho_display = self.largura, self.altura = 640, 640
        self.__fase = None
        self.__teclas_pressionadas = {
            'w':False, 'a':False, 's':False, 'd':False, 'espaco':False
        }
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
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_w:
                self.__teclas_pressionadas['w'] = True
            elif evento.key == pygame.K_a:
                self.__teclas_pressionadas['a'] = True
            elif evento.key == pygame.K_s:
                self.__teclas_pressionadas['s'] = True
            elif evento.key == pygame.K_d:
                self.__teclas_pressionadas['d'] = True
            elif evento.key == pygame.K_SPACE:
                self.__teclas_pressionadas['espaco'] = True
        elif evento.type == pygame.KEYUP:
            if evento.key == pygame.K_w:
                self.__teclas_pressionadas['w'] = False
            elif evento.key == pygame.K_a:
                self.__teclas_pressionadas['a'] = False
            elif evento.key == pygame.K_s:
                self.__teclas_pressionadas['s'] = False
            elif evento.key == pygame.K_d:
                self.__teclas_pressionadas['d'] = False
            elif evento.key == pygame.K_SPACE:
                self.__teclas_pressionadas['espaco'] = False

    def loop(self):
        self.__fase.jogador.decideDirecao(
            self.__teclas_pressionadas['w'], self.__teclas_pressionadas['s'],
             self.__teclas_pressionadas['d'], self.__teclas_pressionadas['a'])

        for inim in (*self.__fase.inimigos_pessoa, *self.__fase.inimigos_obstaculo):
            inim.decideDirecao()

        self.__fase.movimento()

    def renderizar(self):
        self.__fase.mapa.desenhar(self.__display)
        for inim in (*self.__fase.inimigos_pessoa, *self.__fase.inimigos_obstaculo):
            inim.desenhar(self.__display)
        self.fase.jogador.desenhar(self.__display)
        #self.fase.inimigos_pessoa.desenhar(self.__display)
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
            #self.colisao()
        self.limpar()
    
    #CONTROLADOR
    def novaFase(self, nivel_atual:str, dificuldade:float):
        self.__fase = ConstrutorFase.constroiFase(nivel_atual, dificuldade)
    #VITORIA E DERROTA  

    def mostra_texto(self, texto, tamanho, x, y ): 
        pass
    
    def colisao(self): #Enquanto não há obstáculos no mapa 
        if self.fase.jogador.colliderect(self.fase.inimigos_pessoa):
            self.fase.jogador.coord.x -= 1
            self.fase.jogador.coord.y -= 1
    
        


