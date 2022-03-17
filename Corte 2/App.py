from repartidor import Repartidor
import random
import matplotlib.pyplot as plt

# breakpoint()
x = random.randint(-10, 10)
y = random.randint(-10, 10)

clase = Repartidor(x, y, local=[0, 0], cliente=[x * -1, y * -1])

# breakpoint()
for i in range(len(clase.destinos)):
    while clase.x != clase.destinos[i][0] or clase.y != clase.destinos[i][1]:
        clase.elegirDireccion(i)
# breakpoint()
plt.figure(figsize=(15, 10))

ax = plt.subplot(1, 1, 1)

ax.set_title('Mapa de ciudades generadas')

ax.plot(-10, -10, marker='o', lw=0, visible=False)
ax.plot(10, 10, marker='o', lw=0, visible=False)

for ruta in clase.ruta:
    # breakpoint()
    for coord in ruta:
        ax.plot(coord[0], coord[1], marker='o', lw=0)
        x = ruta.index(coord)
        if x != len(ruta) - 1:
            nombre = x.__str__()
            plt.annotate(nombre,
                         (ruta[x + 1][0], ruta[x + 1][1]),
                         (ruta[x][0], ruta[x][1]),
                         arrowprops=dict(facecolor='green', shrink=1)
                         )

plt.show()

print(clase.ruta)
