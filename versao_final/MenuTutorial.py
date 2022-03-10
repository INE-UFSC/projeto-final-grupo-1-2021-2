
from pygame.locals import *
from Menu import Menu

class MenuTutorial(Menu):
    def __init__(self):
        pass
           
    def display_menu(self):
        self.desenha_texto('Tutorial', 40, self.largura / 2,
                           self.altura / 2 - 120, self.__branco, self.__fonte)
        self.desenha_texto("Andar para Direira:  D", 15, self.largura/2,
                           self.altura/2 - 30, self.__branco, self.__fonte)
        self.desenha_texto("Andar para Esquerda: A", 15, self.largura/2,
                           self.altura/2, self.__branco, self.__fonte)
        self.desenha_texto("Andar para Cima: W", 15, self.largura/2,
                           self.altura/2 + 30, self.__branco, self.__fonte)
        self.desenha_texto("Andar para Baixo: S", 15, self.largura/2,
                           self.altura/2 + 60, self.__branco, self.__fonte)
        self.desenha_texto("Pegar Item: Espaço", 15, self.largura/2,
                           self.altura/2 + 90, self.__branco, self.__fonte)
        self.desenha_texto("Entregar Item: Espaço", 15, self.largura/2,
                           self.altura/2 + 120, self.__branco, self.__fonte)
        self.desenha_texto("Voltar: A", 10, self.largura/2 - 200,
                           self.altura/2 + 190, self.__branco, self.__fonte)
        self.desenha_texto("Avançar: D", 10, self.largura/2 + 200,
                           self.altura/2 + 190, self.__branco, self.__fonte)
