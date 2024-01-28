class Multimedia:
    def __init__(self, nombre, anio):
        self._nombre = nombre.title()
        self.anio = anio
        self._me_gusta = 0

    @property
    def nombre(self):
        return self._nombre
    
    @property
    def me_gusta(self):
        return self._me_gusta
    
    #Setting for name
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre.title()

    def gusta(self):
        self._me_gusta += 1



class Pelicula(Multimedia):
    def __init__(self, nombre, anio, duracion):
        super().__init__(nombre, anio)
        self.duracion = duracion
        self._me_gusta = 0



class Serie(Multimedia):
    def __init__(self, nombre, anio, temporadas):
        super().__init__(nombre, anio)
        self.temporadas = temporadas
        self._me_gusta = 0



#creando los objetos

spr = Pelicula('Salvando al soldado ryan', 1998, 170)
hl = Serie('Heartland', 2007, 16)

print(f'El nombre de la pelicula es: {spr.nombre} - el año: {spr.anio} - la duración: {spr.duracion} minutos. Cantidad Likes: {spr.me_gusta}')
print(f'El nombre de la serie es: {hl.nombre} - el año: {hl.anio} - el numero de temporadas: {hl.temporadas}. Cantidad Likes: {hl.me_gusta}')

