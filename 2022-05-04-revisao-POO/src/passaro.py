
class Passaro():

    def __init__(self, distancia, tempo):
        self.__distancia = distancia
        self.__tempo = tempo

    def calcula_velocidade(self):
        return self.__distancia/self.__tempo

    def incrementa_tempo(self, incremento: int):
        self.__tempo += incremento

    def incrementa_distancia(self, incremento: int):
        self.__distancia += incremento
