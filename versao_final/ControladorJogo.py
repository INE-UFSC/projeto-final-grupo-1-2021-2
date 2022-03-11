
import pygame
import time
from pygame.locals import *
from Fase import Fase
from ConstrutorFase import ConstrutorFase
from InimigoPessoa import InimigoPessoa
from Jogador import Jogador
from Item import Item
from PontoEntrega import PontoEntrega
# from Menu import Menu
# from MenuCreditos import MenuCreditos
# from MenuPrincipal import MenuPrincipal
# from MenuTutorial import MenuTutorial
from Camera import Camera
from Estados import EstadosControlador


class ControladorJogo:
    # , fase : Fase, tempo_restante : int, nivel_atual : int, dificuldade : int):
    def __init__(self):
        self.__rodando = True
        self.__display = None
        self.tamanho_display = self.largura, self.altura = 720*2, 400*2
        self.__fase = None
        self.__nivel_atual = None
        self.__dificuldade = None
        self.__teclas_pressionadas = { #True enquanto pressionadas
            'w': False, 'a': False, 's': False, 'd': False, 'espaco': False, 'esc': False}
        self.__teclas_clicadas = { #True somente por 1 frame quando soltas
            'w': False, 'a': False, 's': False, 'd': False, 'espaco': False, 'esc': False}
        self.__timer_font = None
        self.__timer_sec = 60
        self.__timer_text = None
        self.__timer = None
        self.__fps = 60
        self.__timer_fps = pygame.time.Clock()
        # self.__menu = Menu(self.__display)
        # self.__menu_prin = MenuPrincipal(self.__display)
        # self.__menu_crd = MenuCreditos()
        # self.__menu_tut = MenuTutorial()
        self.__fonte = 'PressStart2P-vaV7.ttf'
        self.__estados = {'principal': True, 'tutorial': False,
                          'creditos': False, 'jogo': False, 'game_over': False}
        self.__camera = None
        self.altura_jogar = self.altura/2
        self.altura_tutorial = self.altura/2 + 40
        self.altura_creditos = self.altura/2 + 80
        self.altura_sair = self.altura/2 + 120
        self.distancia_cursor = self.largura/2 - 100
        '''
        self.__tempo_restante = tempo_restante
        self.__nivel_atual = nivel_atual
        self.__dificuldade = dificuldade
        '''
        self.__estado_jogo = EstadosControlador(1) #'menus', 'jogando', 'pause'

    # GETTERS

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

    # LOOP

    def inicializar(self):
        pygame.init()
        self.__display = pygame.display.set_mode(
            self.tamanho_display, pygame.HWSURFACE)
        self.__rodando = True
        self.__jogando = False
        self.__timer_font = pygame.font.Font("freesansbold.ttf", 38)
        # self.__timer_text = self.__timer_font.render(
        # "01:00", True, ((255, 255, 255)))
        self.__timer = pygame.USEREVENT + 1
        self.proxima_fase()
        #pygame.time.set_timer(self.__timer, 1000)
        # self.novaFase()
        self.opcao = 'Jogar'
        self.cursor_rect = pygame.Rect(
            self.distancia_cursor, self.altura/2, 130, 130)
        #self.__camera = Camera(self.fase.jogador.rect, self.tamanho_display)

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
            elif evento.key == pygame.K_ESCAPE:
                self.__teclas_pressionadas['esc'] = True

        elif evento.type == pygame.KEYUP:
            if evento.key == pygame.K_w:
                self.__teclas_pressionadas['w'] = False
                self.__teclas_clicadas['w'] = True
            elif evento.key == pygame.K_a:
                self.__teclas_pressionadas['a'] = False
                self.__teclas_clicadas['a'] = True
            elif evento.key == pygame.K_s:
                self.__teclas_pressionadas['s'] = False
                self.__teclas_clicadas['s'] = True
            elif evento.key == pygame.K_d:
                self.__teclas_pressionadas['d'] = False
                self.__teclas_clicadas['d'] = True
            elif evento.key == pygame.K_SPACE:
                self.__teclas_pressionadas['espaco'] = False
                self.__teclas_clicadas['espaco'] = True
            elif evento.key == pygame.K_ESCAPE:
                self.__teclas_pressionadas['esc'] = False
                self.__teclas_clicadas['esc'] = True

        elif evento.type == self.__timer and int(self.__estado_jogo) == 1: # se for do timer e se estiver jogando
            if self.__timer_sec > 0:
                self.__timer_sec -= 1
                self.__timer_text = self.__timer_font.render(time.strftime(
                    '%M:%S', time.gmtime(self.__timer_sec)), True, ((255, 255, 255)))
            else:
                pygame.time.set_timer(self.__timer, 0)
                self.__jogando = False
                self.__estados['jogo'] = False
                if self.__fase.vitoria == True:
                    self.__estados['principal'] = True

    def loop(self):
        if int(self.__estado_jogo) == 1: #jogando
            self.__fase.movimento(self.__teclas_pressionadas)
            if self.__fase.gerenciamentoItem(self.__teclas_pressionadas['espaco']):
                pass            
            self.__fase.colisao_moveis()
            self.__camera.moverCamera()
            if self.__teclas_clicadas['esc']:
                self.__estado_jogo = EstadosControlador(2)
            #timer do jogo
        
        elif int(self.__estado_jogo) == 0: #menus
            #colocar acoes do menu aqui
            pass

        elif int(self.__estado_jogo) == 2: #pause
            #colocar acoes de pause aqui
            if self.__teclas_clicadas['esc']:
                self.__estado_jogo = EstadosControlador(1)

        if True in self.__teclas_clicadas.values():
            for k in self.__teclas_clicadas.keys():
                self.__teclas_clicadas[k] = False

    def renderizar(self):
        if int(self.__estado_jogo) == 1: #jogando
            #renderizar jogo
            #renderizar interface
            pass

        elif int(self.__estado_jogo) == 0: #menus
            #renderizar menu
            pass

        elif int(self.__estado_jogo) == 2: #pause
            #rederizar jogo um pouco mais escuro
            #renderizar menu de pause
            pass

        self.MudaEstados()
        if self.__estados['principal'] == True:
            self.__display.fill((0, 0, 0))
            self.MenuPrincipal()
            self.move_cursor()
        elif self.__estados['creditos'] == True:
            self.__display.fill((0, 0, 0))
            self.MenuCreditos()
        elif self.__estados['tutorial'] == True:
            self.__display.fill((0, 0, 0))
            self.MenuTutorial()
        elif self.__jogando == True and self.__estados['jogo'] == True:
            self.__display.fill((0, 0, 0))
            self.__fase.mapa.desenhar(
                self.__display, self.__camera.posicao_int)

            if isinstance(self.__fase.ponto_entrega_ativo, PontoEntrega):
                self.__fase.ponto_entrega_ativo.desenhar(
                    self.__display, self.__camera.posicao_int)

            for inim in (*self.__fase.inimigos_pessoa, *self.__fase.inimigos_obstaculo):
                inim.desenhar(self.__display, self.__camera.posicao_int)
            self.__fase.jogador.desenhar(
                self.__display, self.__camera.posicao_int)

            if isinstance(self.__fase.item_ativo, Item) and self.__fase.item_ativo.ativo:
                self.__fase.item_ativo.desenhar(
                    self.__display, self.__camera.posicao_int)
            self.__display.blit(self.__timer_text, (self.altura-160, 20))

            if self.__fase.vitoria == True:
                self.desenha_texto("Vitória!", 50, self.largura/2,
                                   self.altura/2 - 50, ((138, 47, 47)), self.__fonte)
                self.proxima_fase()

        elif self.__fase.vitoria != True and self.__jogando == False:
            #self.proxima_fase()
            self.__display.fill((0, 0, 0))
            self.__estados['game_over'] = True
            self.desenha_texto("Game Over", 50, self.largura/2,
                               self.altura/2, ((138, 47, 47)), self.__fonte)
            self.desenha_texto("Aperte A para retornar ao Menu Principal", 12,
                               self.largura/2, self.altura/2 + 80, ((255, 255, 255)), self.__fonte)
            if self.__teclas_pressionadas['a'] == True:
                self.__estados['principal'] = True
        '''    else:
                self.inicializar() == False'''
        pygame.display.flip()

    def limpar(self):
        pygame.quit()

    def executar(self):  # def que substitui a execucaoFase
        if self.inicializar() == False:
            self.__rodando = False

        while self.__rodando:
            for evento in pygame.event.get():
                self.eventos(evento)
            self.loop()
            self.renderizar()
            self.__timer_fps.tick(self.__fps)
            # self.proxima_fase()
            # NAO COLOQUE CODIGO AQUI, COLOQUE OU NO LOOP() OU NO RENDERIZAR() (DEPENDENDO DO PROPOSITO)!
        self.limpar()

    # CONTROLADOR
    def novaFase(self):
        self.decide_fase()
        self.__fase = ConstrutorFase().constroiFase(
            self.__nivel_atual, self.__dificuldade)
        self.reinicia_timer()
        self.__camera = Camera(self.__fase.jogador.rect, self.tamanho_display)
        print(self.__nivel_atual)

    def decide_fase(self):
        self.__dificuldade = 0
        if self.__fase == None:
            self.__nivel_atual = 'mercado'
        elif self.__fase.vitoria == True:
            if self.__nivel_atual == 'mercado':
                self.__nivel_atual = 'cozinha'
            elif self.__nivel_atual == 'cozinha':
                self.__nivel_atual = 'restaurante'
            else:
                self.__nivel_atual = 'mercado'

    def proxima_fase(self):
        # if self.__jogando == False:
        self.novaFase()

    def desenha_texto(self, texto, tamanho, x, y, cor, fonte):
        font = pygame.font.Font(fonte, tamanho)
        text_surface = font.render(texto, True, cor)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.__display.blit(text_surface, text_rect)

    def move_cursor(self):  # Movimentação do Cursor (Setinha)
        if self.__teclas_pressionadas['s'] == True:
            if self.opcao == 'Jogar':
                self.cursor_rect.midtop = (
                    self.distancia_cursor, self.altura_tutorial)
                self.opcao = 'Tutorial'
                self.__teclas_pressionadas['s'] = False
            elif self.opcao == 'Tutorial':
                self.cursor_rect.midtop = (
                    self.distancia_cursor, self.altura_creditos)
                self.opcao = 'Créditos'
                self.__teclas_pressionadas['s'] = False
            elif self.opcao == 'Créditos':
                self.cursor_rect.midtop = (
                    self.distancia_cursor, self.altura_sair)
                self.opcao = 'Sair'
                self.__teclas_pressionadas['s'] = False
            elif self.opcao == 'Sair':
                self.cursor_rect.midtop = (
                    self.distancia_cursor, self.altura_jogar)
                self.opcao = 'Jogar'
                self.__teclas_pressionadas['s'] = False
        elif self.__teclas_pressionadas['w'] == True:
            if self.opcao == 'Jogar':
                self.cursor_rect.midtop = (
                    self.distancia_cursor, self.altura_sair)
                self.opcao = 'Sair'
                self.__teclas_pressionadas['w'] = False
            elif self.opcao == 'Sair':
                self.cursor_rect.midtop = (
                    self.distancia_cursor, self.altura_creditos)
                self.opcao = 'Créditos'
                self.__teclas_pressionadas['w'] = False
            elif self.opcao == 'Créditos':
                self.cursor_rect.midtop = (
                    self.distancia_cursor, self.altura_tutorial)
                self.opcao = 'Tutorial'
                self.__teclas_pressionadas['w'] = False
            elif self.opcao == 'Tutorial':
                self.cursor_rect.midtop = (
                    self.distancia_cursor, self.altura_jogar)
                self.opcao = 'Jogar'
                self.__teclas_pressionadas['w'] = False

    def MenuPrincipal(self):
        self.desenha_texto('Nome do Jogo', 40, self.largura / 2,
                           self.altura / 8, ((255, 255, 255)), self.__fonte)
        self.desenha_texto("  Menu Principal ", 25, self.largura / 2,
                           self.altura / 4, ((255, 255, 255)), self.__fonte)
        self.desenha_texto("Jogar", 20, self.largura/2,
                           self.altura_jogar, ((255, 255, 255)), self.__fonte)
        self.desenha_texto("Tutorial", 20, self.largura/2,
                           self.altura_tutorial, ((255, 255, 255)), self.__fonte)
        self.desenha_texto("Créditos", 20, self.largura/2,
                           self.altura_creditos, ((255, 255, 255)), self.__fonte)
        self.desenha_texto("Sair", 20, self.largura/2,
                           self.altura_sair, ((255, 255, 255)), self.__fonte)
        self.desenha_texto("Voltar: A", 20, self.largura/2 - 200,
                           self.altura/2 + 190, ((255, 255, 255)), self.__fonte)
        self.desenha_texto("Avançar: D", 20, self.largura/2 + 200,
                           self.altura/2 + 190, ((255, 255, 255)), self.__fonte)
        self.desenha_texto('▶', 20, self.cursor_rect.x,
                           self.cursor_rect.y, ((255, 255, 255)), self.__fonte)

    def MenuCreditos(self):
        self.desenha_texto('Créditos', 20, self.largura / 2,
                           self.altura / 4 - 20, (255, 255, 255), self.__fonte)
        self.desenha_texto('Arthur Torres de Lino', 15, self.largura / 2,
                           self.altura / 2 + 10, (255, 255, 255), self.__fonte)
        self.desenha_texto('Brenda Silva Machado', 15, self.largura / 2,
                           self.altura / 2 + 50, (255, 255, 255), self.__fonte)
        self.desenha_texto('Gabriela Furtado da Silveira', 15, self.largura /
                           2, self.altura / 2 + 90, (255, 255, 255), self.__fonte)
        self.desenha_texto("Voltar: A", 10, self.largura/2 - 200,
                           self.altura/2 + 190, (255, 255, 255), self.__fonte)
        self.desenha_texto("Avançar: D", 10, self.largura/2 + 200,
                           self.altura/2 + 190, (255, 255, 255), self.__fonte)

    def MenuTutorial(self):
        self.desenha_texto('Tutorial', 40, self.largura / 2,
                           self.altura / 2 - 120, (255, 255, 255), self.__fonte)
        self.desenha_texto("Andar para Direira:  D", 15, self.largura/2,
                           self.altura/2 - 30, (255, 255, 255), self.__fonte)
        self.desenha_texto("Andar para Esquerda: A", 15, self.largura/2,
                           self.altura/2, (255, 255, 255), self.__fonte)
        self.desenha_texto("Andar para Cima: W", 15, self.largura/2,
                           self.altura/2 + 30, (255, 255, 255), self.__fonte)
        self.desenha_texto("Andar para Baixo: S", 15, self.largura/2,
                           self.altura/2 + 60, (255, 255, 255), self.__fonte)
        self.desenha_texto("Pegar Item: Espaço", 15, self.largura/2,
                           self.altura/2 + 90, (255, 255, 255), self.__fonte)
        self.desenha_texto("Entregar Item: Espaço", 15, self.largura/2,
                           self.altura/2 + 120, (255, 255, 255), self.__fonte)
        self.desenha_texto("Voltar: A", 10, self.largura/2 - 200,
                           self.altura/2 + 190, (255, 255, 255), self.__fonte)
        self.desenha_texto("Avançar: D", 10, self.largura/2 + 200,
                           self.altura/2 + 190, (255, 255, 255), self.__fonte)

    def MudaEstados(self):
        if self.__estados['principal'] == True:
            self.__estados['tutorial'] = False
            self.__estados['creditos'] = False
            self.__estados['jogo'] = False
        if self.__estados['jogo'] == False:
            if self.__teclas_pressionadas['d'] == True:
                if self.opcao == 'Jogar':
                    # self.proxima_fase()
                    self.__estado_jogo = EstadosControlador(1) #jogando
                    self.__jogando = True
                    self.__estados['jogo'] = True
                    self.__estados['principal'] = False
                    self.reinicia_timer()
                elif self.opcao == 'Tutorial':
                    self.__estados['principal'] = False
                    self.__estados['tutorial'] = True
                elif self.opcao == 'Créditos':
                    self.__estados['principal'] = False
                    self.__estados['creditos'] = True
                elif self.opcao == 'Sair':
                    self.__rodando = False
            elif self.__teclas_pressionadas['a'] == True:
                if self.__estados['tutorial'] == True:
                    self.__estados['principal'] = True
                    self.__estados['tutorial'] = False
                elif self.__estados['creditos'] == True:
                    self.__estados['principal'] = True
                    self.__estados['creditos'] = False

    def reinicia_timer(self):
        self.__timer_sec = 120
        self.__timer_text = self.__timer_font.render(
            "02:00", True, ((255, 255, 255)))
        pygame.time.set_timer(self.__timer, 1000)
    # vou chamar o metodo dentro do mudo estados, para que toda vez que o jogo inicie
    # o timer seja reiniciado
