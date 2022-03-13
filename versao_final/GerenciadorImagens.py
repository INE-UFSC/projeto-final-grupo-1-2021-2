from Singleton import Singleton
import pygame
import os


class GerenciadorImagens(metaclass=Singleton):
    def __init__(self):
        self.__local_imagens = {
            #esses são exemplos, colocar a localização real dos arquivos
            #diretorio de referencia: versao_final/sprites (colocar as imagens/pastas dentro)
            #vamos seguir uma estrutura que cada um é um dicionario?
            'jogador':{
                'teste':'teste.PNG' #'parado1':None, 'parado2':None, etc
            },
            'supermercado':{
                'mapa':'Supermercado/Mapa_supermercado.png' , 'balcao1': 'Supermercado/Balcao_G_vazio.png',
                'balcao2': 'Supermercado/Balcao_G_verduras.png', 'balcao3': 'Supermercado/Balcao_P_frutas.png',
                'balcao4': 'Supermercado/Balcao_P_verduras.png', 'freezer1': 'Supermercado/Freezer_C_fechado.png',
                'freezer2': 'Supermercado/Freezer_C_pacotes.png', 'prateleira1': 'Supermercado/Prateleira_C_caixas.png',
                'prateleira2': 'Supermercado/Prateleira_C_garrafas.png', 'prateleira3': 'Supermercado/Prateleira_G_vazia.png'
            }, #É um dos inimigos_obstáculo, tem frames
            'carrinho_compras' : {
                'carrinho_direita': 'Supermercado/Carrinho_direita.png', 'carrinho_esquerda': 'Supermercado/Carrinho_esquerda.png',
                 'carrinho_frente': 'Supermercado/Carrinho_frente_e_tras.png', 'carrinho_tras': 'Supermercado/Carrinho_frente_e_tras.png'

            },
            'cozinha':{
                'mapa':'Cozinha/Mapa_cozinha.png' , 'balcao1': 'Cozinha/Balcao_comprido_vazio.png',
                'balcao2': 'Cozinha/Balcao_G_cheio.png', 'balcao3': 'Cozinha/Balcao_m_vazio.png',
                'balcao4': 'Cozinha/Balcao_p_utensilio.png', 'balcao5': 'CozinhaBalcao_p.png',
                'geladeira': 'Cozinha/Geladeira.png', 'fogao': 'Cozinha/Fogao.png'
            }, #Inimigo obstaculo
            'carrinho_limpeza' : {
                'carrinho_direita': 'Cozinha/Carrinho_limpeza_direita.png', 'carrinho_esquerda': 'Cozinha/Carrinho_limpeza_esquerda.png',
                 'carrinho_frente': 'Cozinha/Carrinho_limpeza_frente.png', 'carrinho_tras': 'Cozinha/Carrinho_limpeza_tras.png'
            
            },
            'item' : {
                'acucar': 'Comida/Acucar.png', 'alho': 'Comida/Alho.png', 'carne': 'Comida/Carne.png', 
                'leite': 'Comida/Leite.png','manteiga': 'Comida/Manteiga.png', 'ovo': 'Comida/Ovo.png', 
                'pacote': 'Comida/Pacote.png', 'queijo': 'Comida/Queijo.png','tomate': 'Comida/Tomate.png', 
                'churrasco': 'Comida/Churrasco.png', 'macarronada': 'Comida/Macarronada.png', 'salada': 'Comida/Salada.png',
                 'sopa': 'Comida/Sopa.png', 'sorvete': 'Comida/Sorvete.png'
            }
        }
        self.__imagens_carregadas = None
        self.__carregarImagens()

    #vai gerar um dicionario com a mesma hierarquia que o self.__local_imagens, só que com as imagens carregadas
    def __carregarImagens(self):
        imagens = {}
        for componente, sprites in self.__local_imagens.items():
            imagens[componente] = {}
            for descricao, sprite in sprites.items():
                imagens[componente][descricao] = pygame.image.load(os.path.join('versao_final', 'sprites', sprite))
                imagens[componente][descricao].convert_alpha() #deixa as imagens PNG transparentes

        self.__imagens_carregadas = imagens

    def getSprite(self, componente:str, descricao:str)->pygame.image:
        return self.__imagens_carregadas[componente][descricao]