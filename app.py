
class Pelicula:
    def __init__(self, nombre, anio, duracion):
        self.nombre = nombre.title()
        self.anio = anio
        self.duracion = duracion
        self.me_gusta = 0

    def gusta(self):
        self.me_gusta += 1


class Serie:
    def __init__(self, nombre, anio, temporadas):
        self.nombre = nombre.title()
        self.anio = anio
        self.temporadas = temporadas
        self.me_gusta = 0

    def gusta(self):
        self.me_gusta += 1


#creando los objetos

spr = Pelicula('Salvando al soldado ryan', 1998, 170)
hl = Serie('Heartland', 2007, 16)

print(f'El nombre de la pelicula es: {spr.nombre} - el año: {spr.anio} - la duración: {spr.duracion} minutos. Cantidad Likes: {spr.me_gusta}')
print(f'El nombre de la serie es: {hl.nombre} - el año: {hl.anio} - el numero de temporadas: {hl.temporadas}. Cantidad Likes: {hl.me_gusta}')

