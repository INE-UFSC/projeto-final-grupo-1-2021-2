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
                'teste': 'teste.png'  # 'parado1':None, 'parado2':None, etc
            },
            'mapa': {
                'mercado': 'Supermercado/Mapa_supermercado.png'
            },
            'obstaculo': {
                'balcao_vertical': 'Supermercado/balcao_comprido.png',
                'balcao_horizontal': 'Supermercado/balcao_deitado.png',
                'balcao_grande_comida': 'Supermercado/balcao_grande_cheio.png',
                'caixa': 'Supermercado/caixa_grande.png',
                'caixas_grandes': 'Supermercado/caixas_grandes.png',
                'mostruario_vertical_vazio': 'Supermercado/mostruario_comprido_vazio.png',
                'mostruario_vertical_cheio': 'Supermercado/mostruario_comprido.png',
                'mostruario_G_cheio': 'Supermercado/mostruario_grande_cheio.png',
                'mostruario_G_vazio': 'Supermercado/mostruario_grande_vazio.png',
                'placa_sale': 'Supermercado/placa_sale.png',
                'prateleira_horizontal': 'Supermercado/prateleira_deitada.png',
                'prateleira_M_cheia1': 'Supermercado/prateleira_cortada.png',
                'prateleira_M_vazia': 'Supermercado/prateleira_grande_vazia.png',
                'prateleira_M_cheia2': 'Supermercado/prateleira_media_cheia1.png',
                'prateleira_M_cheia3': 'Supermercado/prateleira_media_cheia2.png',
                'tijolos_vermelhos_cima': 'Supermercado/tijolos_vermelhos_cima.png',
                'tijolos_vermelhos_baixo': 'Supermercado/tijolos_vermelhos_baixo.png',
                'tijolos_vermelhos_esquerda': 'Supermercado/tijolos_vermelhos_esquerda.png',
                'tijolos_vermelhos_direita': 'Supermercado/tijolos_vermelhos_direita.png'

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
