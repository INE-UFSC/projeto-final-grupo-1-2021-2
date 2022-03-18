from enum import IntEnum

class Estados(IntEnum):
    JOGANDO = 0
    PRINCIPAL = 1 
    DIFICULDADE = 2   
    TUTORIAL = 3
    CREDITOS = 4
    VITORIA = 5
    DERROTA = 6
    PAUSA = 7


class EstadosMenus(IntEnum):
    PRINCIPAL = 0
    TUTORIAL = 1
    CREDITOS = 2
    VITORIA = 3
    DERROTA = 4
    PAUSA = 5 #?