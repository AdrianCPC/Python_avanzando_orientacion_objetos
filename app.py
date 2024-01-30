class Playlist:
    def __init__(self, nombre, multimedia):
        self._nombre = nombre
        self._multimedia = multimedia

    #@property
    #def lista(self):
        #return self._multimedia
    #@property
    #def tamano(self):
        #return len(self._multimedia)

#using dunder (duck typing)
    def __getitem__(self, item):
        return self._multimedia[item]
    

    def __len__(self):
        return len(self._multimedia)




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

    #polimorfismo
    #def imprime(self):
        #print(f'{self.nombre} - {self.anio} - {self._me_gusta} Likes')
    def __str__(self):
        return f'{self.nombre} - {self.anio} - {self._me_gusta} Likes'


class Pelicula(Multimedia):
    def __init__(self, nombre, anio, duracion):
        super().__init__(nombre, anio)
        self.duracion = duracion
        self._me_gusta = 0

    #def imprime(self):
        #print(f'{self.nombre} - {self.anio} - {self.duracion} min - {self._me_gusta} Likes')
    def __str__(self):
        return f'{self.nombre} - {self.anio} - {self.duracion} min - {self._me_gusta} Likes'


class Serie(Multimedia):
    def __init__(self, nombre, anio, temporadas):
        super().__init__(nombre, anio)
        self.temporadas = temporadas
        self._me_gusta = 0

    #def imprime(self):
        #print(f'{self.nombre} - {self.anio} - {self.temporadas} temporadas - {self._me_gusta} Likes')
    def __str__(self):
        return f'{self.nombre} - {self.anio} - {self.temporadas} temporadas - {self._me_gusta} Likes'


#creando los objetos

spr = Pelicula('Salvando al soldado ryan', 1998, 170)
hl = Serie('Heartland', 2007, 16)
kb = Pelicula('kill bill', 2002, 120)
dark = Serie('dark', 2016,3)

#print(f'El nombre de la pelicula es: {spr.nombre} - el año: {spr.anio} - la duración: {spr.duracion} minutos. Cantidad Likes: {spr.me_gusta}')
#print(f'El nombre de la serie es: {hl.nombre} - el año: {hl.anio} - el numero de temporadas: {hl.temporadas}. Cantidad Likes: {hl.me_gusta}')


series_peliculas = [spr,hl, kb, dark]

for multimedia in series_peliculas:
    #detalles = multimedia.duracion if hasattr(multimedia,'duracion') else multimedia.temporadas
    #print(f'Nombre: {multimedia.nombre} - Detalles: {detalles} Año: {multimedia.anio}')
    print(multimedia)

playlist_fds = Playlist('Playlist fin de semana', series_peliculas)

for contenido in playlist_fds:
    print(contenido)