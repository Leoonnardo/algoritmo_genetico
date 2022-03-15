
class Local:
    x: int
    y: int
    nombre: str

    def __init__(self, nombre: str, *coordenadas):
        self.nombre = nombre
        self.x = coordenadas[0]
        self.y = coordenadas[1]
