from Singleton import Singleton
import pygame
import os


class GerenciadorImagens(metaclass=Singleton):
    def __init__(self):
        self.__local_imagens = {
            # esses são exemplos, colocar a localização real dos arquivos
            # diretorio de referencia: versao_final/sprites (colocar as imagens/pastas dentro)
            # vamos seguir uma estrutura que cada um é um dicionario?
            'jogador': {
                'teste': 'teste.PNG'  # 'parado1':None, 'parado2':None, etc
            },
            'mapa': {
                'mercado': 'Supermercado/Mapa_supermercado.png'
            },
            'obstaculo': {
                'balcao_G_vazio': 'Supermercado/Balcao_G_vazio.png',
                'balcao_G_verduras': 'Supermercado/Balcao_G_verduras.png',
                'balcao_P_frutas': 'Supermercado/Balcao_P_frutas.png',
                'balcao_P_verduras': 'Supermercado/Balcao_P_verduras.png',
                'freezer_fechado': 'Supermercado/Freezer_C_fechado.png',
                'freezer_pacotes': 'Supermercado/Freezer_C_pacotes.png',
                'prateleira_vazia': 'Supermercado/Prateleira_G_vazia.png',
                'prateleira_caixas': 'Supermercado/Prateleira_C_caixas.png',
                'prateleira_garrafas': 'Supermercado/Prateleira_C_garrafas.png',
                'prateleira': 'prateleira_cortada.png'
            },
            'inimigo_obstaculo': {
                'carrinho_direita': 'Supermercado/Carrinho_direita.png',
                'carrinho_esquerda': 'Supermercado/Carrinho_esquerda.png',
                'carrinho_frente/tras': 'Supermercado/Carrinho_frente_e_tras.png'
            }
            # 'inimigos_pessoa':{}, etc
        }
        self.__imagens_carregadas = None
        self.__carregarImagens()

    # vai gerar um dicionario com a mesma hierarquia que o self.__local_imagens, só que com as imagens carregadas
    def __carregarImagens(self):
        imagens = {}
        for componente, sprites in self.__local_imagens.items():
            imagens[componente] = {}
            for descricao, sprite in sprites.items():
                imagens[componente][descricao] = pygame.image.load(
                    os.path.join('versao_final', 'sprites', sprite))
                # deixa as imagens PNG transparentes
                imagens[componente][descricao].convert_alpha()

        self.__imagens_carregadas = imagens

    def getSprite(self, componente: str, descricao: str, largura: int, altura: int) -> pygame.image:
        imagem = pygame.transform.scale(
            self.__imagens_carregadas[componente][descricao], (largura, altura))
        return imagem
