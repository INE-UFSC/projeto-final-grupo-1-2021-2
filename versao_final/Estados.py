from enum import IntEnum

class EstadosControlador(IntEnum):
    MENUS = 0
    JOGANDO = 1
    PAUSE = 2

class EstadosMenus(IntEnum):
    PRINCIPAL = 0
    TUTORIAL = 1
    CREDITOS = 2
    VITORIA = 3
    DERROTA = 4
    PAUSA = 5 #?