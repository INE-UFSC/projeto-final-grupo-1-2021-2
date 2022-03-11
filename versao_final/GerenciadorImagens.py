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
            }
            #'inimigos_pessoa':{}, etc
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