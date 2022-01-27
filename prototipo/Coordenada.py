class Coordenada:
    def __init__(self, x:float, y:float):
        self.__x = x
        self.__y = y

    @property
    def x(self) -> float:
        return self.__x

    @property
    def y(self) -> float:
        return self.__y

    @x.setter
    def x(self, x:float):
        self.__x = x

    @y.setter
    def y(self, y: float):
        self.__y = y

    def mover(self, x: float, y: float):
        self.__x += x
        self.__y += y

    def calculaDistancia(self, coord) -> float:
        return ((self.__x - coord.x)**2 + (self.__y - coord.y)**2)**0.5