import random



class Repartidor:
    x = 0
    y = 0
    destinoX = 0
    destinoY = 0
    ruta = []
    enLimiteX = False
    enLimiteY = False

    def __int__(self, *coordenadas):
        self.x = coordenadas[0]
        self.y = coordenadas[1]
        self.destinoX = coordenadas[2]
        self.destinoY = coordenadas[3]
        self.ruta.append([self.x, self.y])

    def elegirDireccion(self, limites):
        # Elige la dirección que tomará de manera aleatoria
        # disminuyendo o aumentando una de las coordenadas necesarias para
        # ubicarse en el plano cartesiano
        # Eje: indica sobre que eje se actuará, 0 para abscisas 1 para ordenadas
        # Operador: indica que se hará con dicha coordenada, 1 para aumentar, 0 para disminuir

        limitesX = limites[0]
        limitesY = limites[1]

        self.enLimiteX = self.x == limitesX[0] or self.x == limitesX[1]
        self.enLimiteY = not self.y == limitesY[0] or not self.x == limitesY[1]

        # Pregunta si está en los extremos de las abscisas
        if self.enLimiteX:
            # Pregunta si está sobre el valor más bajo de las abscisas
            if self.x == limitesX[0]:
                # Pregunta si también está en los extremos de las ordenadas
                if self.enLimiteY:
                    # Pregunta si está sobre el valor más bajo de las ordenadas
                    if self.y == limitesY[0]:
                        # Elige entre abscisas u ordenadas
                        eje = random.randint(0, 1)
                        # Define un aumento
                        operador = 1
                        self.__caminar(eje, operador)
                    # En caso de estar sobre el valor más alto de las ordenadas
                    else:
                        # Elige entre abscisas u ordenadas
                        eje = random.randint(0, 1)
                        # Pregunta si el eje es 1
                        if eje:
                            # Define una disminución
                            operador = 0
                            self.__caminar(eje, operador)
                        else:
                            # Define un aumento
                            operador = 1
                            self.__caminar(eje, operador)
                # En caso de no estar sobre el límite de las ordenadas
                else:
                    # Elige entre abscisas u ordenadas
                    eje = random.randint(0, 1)
                    # Pregunta si el eje es 1
                    if eje:
                        # Elige entre aumentar o disminuir
                        operador = random.randint(0, 1)
                        self.__caminar(eje, operador)
                    else:
                        # Define un aumento
                        operador = 1
                        self.__caminar(eje, operador)
            # En caso de estar en el valor más alto de las abscisas
            else:
                # Pregunta si también está en los extremos de las ordenadas
                if self.enLimiteY:
                    # Pregunta si está sobre el valor más bajo de las ordenadas
                    if self.y == limitesY[0]:
                        # Elige entre abscisas u ordenadas
                        eje = random.randint(0, 1)
                        # Pregunta si el eje es 1
                        if eje:
                            # Define un aumento
                            operador = 1
                            self.__caminar(eje, operador)
                        else:
                            # Define una disminución
                            operador = 0
                            self.__caminar(eje, operador)
                        self.__caminar(eje, operador)
                    # En caso de estar sobre el valor más alto de las ordenadas
                    else:
                        # Elige entre abscisas u ordenadas
                        eje = random.randint(0, 1)
                        # Define una disminución
                        operador = 0
                        self.__caminar(eje, operador)
                # En caso de no estar sobre el límite de las ordenadas
                else:
                    # Elige entre abscisas u ordenadas
                    eje = random.randint(0, 1)
                    # Pregunta si el eje es 1
                    if eje:
                        # Elige entre aumentar o disminuir
                        operador = random.randint(0, 1)
                        self.__caminar(eje, operador)
                    else:
                        # Define un aumento
                        operador = 0
                        self.__caminar(eje, operador)
        # En caso de no estar sobre el límite de las abscisas
        else:
            # Pregunta si esta sobre el límite de las ordenadas
            if self.enLimiteY:
                # Pregunta si está sobre el valor más bajo de las ordenadas
                if self.y == limitesY[0]:
                    # Elige entre abscisas u ordenadas
                    eje = random.randint(0, 1)
                    # Pregunta si el eje es 1
                    if eje:
                        # Define un aumento
                        operador = 1
                        self.__caminar(eje, operador)
                    else:
                        # Define una disminución
                        operador = 0
                        self.__caminar(eje, operador)
                # En caso de estar sobre el valor más alto de las ordenadas
                else:
                    # Elige entre abscisas u ordenadas
                    eje = random.randint(0, 1)
                    # Define una disminución
                    operador = 0
                    self.__caminar(eje, operador)
            # En caso de no estar tampoco sobre el límite de las ordenadas
            else:
                # Elige entre abscisas u ordenadas
                eje = random.randint(0, 1)
                # Elige entre aumentar o disminuir
                operador = random.randint(0, 1)
                self.__caminar(eje, operador)

    def __caminar(self, eje, operador):
        if eje == 0:
            if operador:
                self.x += 1
            else:
                self.x -= 1
        else:
            if operador:
                self.y += 1
            else:
                self.y -= 1
        self.ruta.append([self.x, self.y])
