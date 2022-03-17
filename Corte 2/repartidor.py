import random

from typing import List


class Repartidor:
    x: int
    y: int
    destinos = []
    ruta = []
    destinos_visitados = [int]
    pasos: int
    direccion: int
    enLimiteX: bool
    enLimiteY: bool

    def __init__(self, x: int, y: int, **destinos):
        self.x = x
        self.y = y
        for destino in destinos.keys():
            self.destinos.append(destinos[destino])
            self.ruta.append([])
        self.ruta[0].append([self.x, self.y])
        self.pasos = 0

    def elegirDireccion(self, destino):
        # Elige la dirección que tomará de manera aleatoria
        # disminuyendo o aumentando una de las coordenadas necesarias para
        # ubicarse en el plano cartesiano
        # Eje: indica sobre que eje se actuará, 0 para abscisas 1 para ordenadas
        # Operador: indica que se hará con dicha coordenada, 1 para aumentar, 0 para disminuir
        if len(self.ruta[destino]) == 0:
            self.ruta[destino].append([self.x, self.y])

        eje = random.randint(0, 1)

        coords = self.destinos[destino]

        if eje:
            if self.y < coords[eje]:
                operador = 1
                paso = self.__caminar(eje, operador)
                self.__paso(paso, destino)
            elif self.y > coords[eje]:
                operador = 0
                paso = self.__caminar(eje, operador)
                self.__paso(paso, destino)
        elif self.x < coords[eje]:
            operador = 1
            paso = self.__caminar(eje, operador)
            self.__paso(paso, destino)
        elif self.x > coords[eje]:
            operador = 0
            paso = self.__caminar(eje, operador)
            self.__paso(paso, destino)


        # repetido = True
        # limitesX = limites[0]
        # limitesY = limites[1]
        # # breakpoint()
        # self.enLimiteX = self.x == limitesX[0] or self.x == limitesX[1]
        # self.enLimiteY = self.y == limitesY[0] or self.x == limitesY[1]

        # Pregunta si está en los extremos de las abscisas
        # while repetido:
        #     if self.enLimiteX:
        #         # Pregunta si está sobre el valor más bajo de las abscisas
        #         if self.x == limitesX[0]:
        #             # Pregunta si también está en los extremos de las ordenadas
        #             if self.enLimiteY:
        #                 # Pregunta si está sobre el valor más bajo de las ordenadas
        #                 if self.y == limitesY[0]:
        #                     # Elige entre abscisas u ordenadas
        #                     eje = random.randint(0, 1)
        #                     # Define un aumento
        #                     operador = 1
        #                     paso = self.__caminar(eje, operador)
        #                 # En caso de estar sobre el valor más alto de las ordenadas
        #                 else:
        #                     # Elige entre abscisas u ordenadas
        #                     eje = random.randint(0, 1)
        #                     # Pregunta si el eje es 1
        #                     if eje:
        #                         # Define una disminución
        #                         operador = 0
        #                         paso = self.__caminar(eje, operador)
        #                     else:
        #                         # Define un aumento
        #                         operador = 1
        #                         paso = self.__caminar(eje, operador)
        #             # En caso de no estar sobre el límite de las ordenadas
        #             else:
        #                 # Elige entre abscisas u ordenadas
        #                 eje = random.randint(0, 1)
        #                 # Pregunta si el eje es 1
        #                 if eje:
        #                     # Elige entre aumentar o disminuir
        #                     operador = random.randint(0, 1)
        #                     paso = self.__caminar(eje, operador)
        #                 else:
        #                     # Define un aumento
        #                     operador = 1
        #                     paso = self.__caminar(eje, operador)
        #         # En caso de estar en el valor más alto de las abscisas
        #         else:
        #             # Pregunta si también está en los extremos de las ordenadas
        #             if self.enLimiteY:
        #                 # Pregunta si está sobre el valor más bajo de las ordenadas
        #                 if self.y == limitesY[0]:
        #                     # Elige entre abscisas u ordenadas
        #                     eje = random.randint(0, 1)
        #                     # Pregunta si el eje es 1
        #                     if eje:
        #                         # Define un aumento
        #                         operador = 1
        #                         paso = self.__caminar(eje, operador)
        #                     else:
        #                         # Define una disminución
        #                         operador = 0
        #                         paso = self.__caminar(eje, operador)
        #                 # En caso de estar sobre el valor más alto de las ordenadas
        #                 else:
        #                     # Elige entre abscisas u ordenadas
        #                     eje = random.randint(0, 1)
        #                     # Define una disminución
        #                     operador = 0
        #                     paso = self.__caminar(eje, operador)
        #             # En caso de no estar sobre el límite de las ordenadas
        #             else:
        #                 # Elige entre abscisas u ordenadas
        #                 eje = random.randint(0, 1)
        #                 # Pregunta si el eje es 1
        #                 if eje:
        #                     # Elige entre aumentar o disminuir
        #                     operador = random.randint(0, 1)
        #                     paso = self.__caminar(eje, operador)
        #                 else:
        #                     # Define un aumento
        #                     operador = 0
        #                     paso = self.__caminar(eje, operador)
        #     # En caso de no estar sobre el límite de las abscisas
        #     else:
        #         # Pregunta si esta sobre el límite de las ordenadas
        #         if self.enLimiteY:
        #             # Pregunta si está sobre el valor más bajo de las ordenadas
        #             if self.y == limitesY[0]:
        #                 # Elige entre abscisas u ordenadas
        #                 eje = random.randint(0, 1)
        #                 # Pregunta si el eje es 1
        #                 if eje:
        #                     # Define un aumento
        #                     operador = 1
        #                     paso = self.__caminar(eje, operador)
        #                 else:
        #                     # Define una disminución
        #                     operador = 0
        #                     paso = self.__caminar(eje, operador)
        #             # En caso de estar sobre el valor más alto de las ordenadas
        #             else:
        #                 # Elige entre abscisas u ordenadas
        #                 eje = random.randint(0, 1)
        #                 # Define una disminución
        #                 operador = 0
        #                 paso = self.__caminar(eje, operador)
        #         # En caso de no estar tampoco sobre el límite de las ordenadas
        #         else:
        #             if self.direccion is None:
        #                 self.direccion = random.randint(0, 3)
        #             # Verifica la dirección
        #             if self.direccion == 0:
        #                 # Elige entre abscisas y ordenadas
        #                 eje = random.randint(0, 1)
        #                 # Pregunta si el eje es 1
        #                 if eje:
        #                     # Realiza un aumento
        #                     operador = 1
        #                 else:
        #                     # Elige entre disminuir o aumentar
        #                     operador = random.randint(0, 1)
        #                 paso = self.__caminar(eje, operador)
        #             elif self.direccion == 1:
        #                 # Elige entre abscisas y ordenadas
        #                 eje = random.randint(0, 1)
        #                 # Pregunta si el eje es 0
        #                 if not eje:
        #                     # Realiza un aumento
        #                     operador = 1
        #                 else:
        #                     # Elige entre aumentar o disminuir
        #                     operador = random.randint(0, 1)
        #                 paso = self.__caminar(eje, operador)
        #             elif self.direccion == 2:
        #                 eje = random.randint(0, 1)
        #                 if eje:
        #                     operador = 0
        #                 else:
        #                     operador = random.randint(0, 1)
        #                 paso = self.__caminar(eje, operador)
        #             else:
        #                 eje = random.randint(0, 1)
        #                 if not eje:
        #                     operador = 0
        #                 else:
        #                     operador = random.randint(0, 1)
        #                 paso = self.__caminar(eje, operador)
        #
        #     # breakpoint()
        #     if not self.__eval(paso):
        #         repetido = False
        #         self.__paso(paso)

    # def __caminar(self, eje, operador):
    #     x = self.x
    #     y = self.y
    #
    #     if eje == 0:
    #         if operador:
    #             x += 1
    #             self.direccion = 1
    #         else:
    #             self.direccion = 3
    #             x -= 1
    #     else:
    #         if operador:
    #             self.direccion = 0
    #             y += 1
    #         else:
    #             self.direccion = 2
    #             y -= 1
    #     return [x, y]
    #
    # def __eval(self, paso):
    #     if self.enLimiteY and self.enLimiteX:
    #         return False
    #     else:
    #         for coords in self.ruta:
    #             if coords[0] == paso[0] and coords[1] == paso[0]:
    #                 return True
    #             if self.ruta.index(coords) == self.pasos:
    #                 return False

    def __caminar(self, eje, operador):
        x = self.x
        y = self.y

        if eje == 0:
            if operador:
                x += 1
            else:
                x -= 1
        else:
            if operador:
                y += 1
            else:
                y -= 1
        return [x, y]

    def __paso(self, paso, destino):
        if not self.__eval(paso, destino):
            self.ruta[destino].append(paso)
            self.x = paso[0]
            self.y = paso[1]
            self.pasos += 1

    def __eval(self, paso, destino):
        # breakpoint()
        for coords in self.ruta[destino]:
            if coords[0] == paso[0] and coords[1] == paso[1]:
                return True
            if self.ruta[destino].index(coords) == len(self.ruta[destino]) - 1:
                return False
