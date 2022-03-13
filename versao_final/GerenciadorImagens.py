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
                'mapa':'Supermercado/Mapa_supermercado.png' , 'balcao1': 'Supermercado/balcao_deitado.png',
                'balcao2': 'Supermercado/balcao_comprido.png', 'balcao3': 'Supermercado/balcao_grande_cheio.png',
                'caixa': 'Supermercado/caixa_grande.png', 'caixotes': 'Supermercado/caixas_grandes.png',
                'placa_sale': 'Supermercado/placa_sale.png', 'prateleira1': 'Supermercado/prateleira_deitada.png',
                'prateleira2': 'Supermercado/prateleira_grande_vazia.png', 'prateleira3': 'Supermercado/prateleira_media_cheia1.png'
                'prateleira4': 'Supermercado/prateleira_media_cheia2.png' , 'prateleira5': 'Supermercado/prateleira_media_vazia.png',
                'mostruario1': 'Supermercado/mostruario_comprido.png', 'mostruario2': 'Supermercado/mostruario_comprido_vazio.png',
                'mostruario3': 'Supermercado/mostruario_grande_cheio.png', 'mostruario1': 'Supermercado/mostruario_grande_vazio.png',
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
                #ingredientes
                'acucar': 'Comida/acucar.png', 'alho': 'Comida/alho.png', 'carne_crua': 'Comida/carne_crua.png', 
                'leite': 'Comida/leite.png','manteiga': 'Comida/manteiga.png', 'ovo': 'Comida/ovo.png', 
                'pacote': 'Comida/pacote.png', 'queijo': 'Comida/queijo.png','tomate': 'Comida/tomate.png',
                'alface': 'Comida/alface.png', 'batata': 'Comida/batata.png', 'cebola': 'Comida/cebola.png',
                'peixe': 'Comida/peixe.png', 'pote': 'Comida/pote.png','taco': 'Comida/taco.png',
                #pratos
                'carne_assada': 'Comida/carne_assada.png', 'macarronada': 'Comida/macarronada.png','pizza': 'Comida/pizza.png',
                'sopa': 'Comida/sopa.png', 'taco': 'Comida/taco.png', 'bolo': 'Comida/bolo.png','panqueca': 'Comida/panqueca.png',
                'torta_fruta': 'Comida/torta_fruta.png', 'suco_limao': 'Comida/suco_limao.png','pudim': 'Comida/pudim.png',
                'suco_morango': 'Comida/suco_morango.png', 'sanduiche': 'Comida/sanduiche.png',
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
