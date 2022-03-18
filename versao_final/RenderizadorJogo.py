from cgitb import text
from typing import Tuple
import pygame
import sys
from pygame.locals import *
from GerenciadorImagens import GerenciadorImagens
from Mapa import Mapa
from PontoEntrega import PontoEntrega
from Item import Item
from InimigoObstaculo import InimigoObstaculo
from InimigoPessoa import InimigoPessoa
from Jogador import Jogador
from Coordenada import Coordenada
from Tamanho import Tamanho


class RenderizadorJogo():
    def __init__(self, tamanho: Tuple):
        self.__tamanho_display = self.__largura, self.__altura = tamanho[0], tamanho[1]
        self.__fonte = 'PressStart2P-vaV7.ttf'

    def renderizar(self, display: pygame.display, posicao_camera: int, mapa: Mapa,
                   ponto_entrega: PontoEntrega, inimigos_p, inimigos_o, jogador: Jogador, item: Item, timer_text):
        display.fill((0, 0, 0))
        for x in mapa.desenhar(posicao_camera):
            display.blit(x[0], x[1])
        if isinstance(ponto_entrega, PontoEntrega):
            dados_pe = ponto_entrega.desenhar(posicao_camera)
            display.blit(dados_pe[0], dados_pe[1])
        for movel in (*inimigos_p, *inimigos_o, jogador):
            dado_mov = movel.desenhar(posicao_camera)
            display.blit(dado_mov[0], dado_mov[1])
        if isinstance(item, Item) and item.ativo:
            dados_item = item.desenhar(posicao_camera)
            display.blit(dados_item[0], dados_item[1])

        rect = timer_text.get_rect()
        rect.topleft = (self.__altura-160, 20)
        pygame.draw.rect(display, (0, 0, 0), rect)  # fundo para o timer
        display.blit(timer_text, (self.__altura-160, 20))  # desenha o timer

        font = pygame.font.Font(self.__fonte, 20)
        text_surface = font.render('Pausar: esc', True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.topleft = (5, 10)
        pygame.draw.rect(display, (0, 0, 0), text_rect.inflate(4, 4).move(-1, -1))
        display.blit(text_surface, text_rect) 

        self.desenhar_bussola_interativos(
            display, posicao_camera, ponto_entrega, item, jogador)

    def desenhar_bussola_interativos(self, display, posicao_camera, ponto_entrega, item, jogador):
        if ponto_entrega != None or item != None:
            if (item != None and item.ativo == True):
                destino = item.coord
                cor = (128, 0, 0)
            elif ponto_entrega != None:
                destino = ponto_entrega.coord
                cor = (255, 140, 0)
            vetor = Coordenada.versorEntreCoordenadas(jogador.coord, destino)

            ponta_triangulo = ((jogador.coord.x+vetor.x*jogador.tamanho.largura*1.5 - posicao_camera.x),
                               (jogador.coord.y+vetor.y*jogador.tamanho.altura*1.5 - posicao_camera.y))
            base_esquerda = ((jogador.coord.x+vetor.x*jogador.tamanho.largura - posicao_camera.x + 5),
                             (jogador.coord.y+vetor.y*jogador.tamanho.altura - posicao_camera.y + 5))
            base_direita = ((jogador.coord.x+vetor.x*jogador.tamanho.largura - posicao_camera.x - 5),
                            (jogador.coord.y+vetor.y*jogador.tamanho.altura - posicao_camera.y - 5))
            pygame.draw.polygon(display, cor, points=[
                                ponta_triangulo, base_direita, base_esquerda])
