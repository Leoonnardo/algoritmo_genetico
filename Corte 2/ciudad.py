import sys
from PySide6.QtCore import *
import matplotlib.pyplot as plt
import random
from PySide6.QtWidgets import *

# from main import ventana

# PARAMETROS PARA LO DE LAS CIUDADES
IntervaloX = [-10, 10]
IntervaloY = [-10, 10]
NoRestaurantes = 6
InicialRestaurante = None
Restaurantes = []
Population = []

# PARAMETROS PARA EL ALGORITMO GENETICO
InitialPopulation = 6
MaxPopulation = 10
ProbMutation = 0.5
ProbMutationGen = 0.05
numGeneration = 20
Generations = {}


def generateCities():
    global InicialRestaurante

    # Generando las ciudades al azar

    i = 0
    while (i < NoRestaurantes):
        currentCity = []

        randX = random.randint(IntervaloX[0], IntervaloX[1])
        randY = random.randint(IntervaloY[0], IntervaloY[1])

        currentCity.append(randX)
        currentCity.append(randY)

        if Restaurantes.count(currentCity) == 0:
            Restaurantes.append(currentCity)
            i += 1

    # Tomando un numero random entre 0 y el total de ciudades para generar la ciudad inicial

    InicialRestaurante = Restaurantes[random.randint(0, len(Restaurantes) - 1)]

def generateFirtsMap():
    generateCities()

    plt.figure(figsize=(15, 10))

    ax = plt.subplot(1, 1, 1)

    ax.set_title('Mapa de ciudades generadas')

    ax.plot(IntervaloX[0], IntervaloY[0], marker='o', lw=0, visible=False)
    ax.plot(IntervaloX[1], IntervaloY[1], marker='o', lw=0, visible=False)


    for x in range(len(Restaurantes)):

        ax.plot(Restaurantes[x][0], Restaurantes[x][1], marker='o', lw=0)

    ax.plot(Restaurantes[0], Restaurantes[1], marker='x', lw=0,color='k')

    plt.show()

# generateCities()
generateFirtsMap()
