from repartidor import Repartidor
import random
import matplotlib.pyplot as plt


x = random.randint(-10, 10)
y = random.randint(-10, 10)

clase = Repartidor()
clase.x = x
clase.y = y
clase.destinoX = 0
clase.destinoY = 0

while clase.x != clase.destinoX or clase.y != clase.destinoY:
    clase.elegirDireccion([[-10, 10], [-10, 10]])

plt.figure(figsize=(15, 10))

ax = plt.subplot(1, 1, 1)

ax.set_title('Mapa de ciudades generadas')

ax.plot(-10, -10, marker='o', lw=0, visible=False)
ax.plot(10, 10, marker='o', lw=0, visible=False)


for x in clase.ruta:
    ax.plot(x[0], x[1], marker='o', lw=0)

plt.show()

print(clase.ruta)
