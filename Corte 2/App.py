from repartidor import Repartidor
import random
import matplotlib.pyplot as plt

x = random.randint(-10, 10)
y = random.randint(-10, 10)

clase = Repartidor(10, 10, local=[0, 0], cliente=[x * -1, y * -1])

# breakpoint()
while clase.x != clase.destinos[0][0] or clase.y != clase.destinos[0][0]:
    clase.elegirDireccion([[-10, 10], [-10, 10]])

plt.figure(figsize=(15, 10))

ax = plt.subplot(1, 1, 1)

ax.set_title('Mapa de ciudades generadas')

ax.plot(-10, -10, marker='o', lw=0, visible=False)
ax.plot(10, 10, marker='o', lw=0, visible=False)

for x in range(clase.pasos):
    ax.plot(clase.ruta[x][0], clase.ruta[x][1], marker='o', lw=0)
    if x != len(clase.ruta) - 1:
        nombre = x.__str__()
        plt.annotate(nombre,
                     (clase.ruta[x + 1][0], clase.ruta[x + 1][1]),
                     (clase.ruta[x][0], clase.ruta[x][1]),
                     arrowprops=dict(
                         arrowstyle='->',
                         facecolor='green')
                     )

plt.show()

print(clase.ruta)
