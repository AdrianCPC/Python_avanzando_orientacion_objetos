
class Pelicula:
    def __init__(self, nombre, anio, duracion):
        self.nombre = nombre
        self.anio = anio
        self.duracion = duracion


class Serie:
    def __init__(self, nombre, anio, temporadas):
        self.nombre = nombre
        self.anio = anio
        self.temporadas = temporadas


#creando los objetos

spr = Pelicula('Salvando al soldado ryan', 1998, 170)
hl = Serie('Heartland', 2007, 16)

print(f'El nombre de la pelicula es: {spr.nombre} - el año: {spr.anio} - la duración: {spr.duracion} minutos')
print(f'El nombre de la serie es: {hl.nombre} - el año: {hl.anio} - el numero de temporadas: {hl.temporadas}')
