usuarios_ds = [15,23,43,56]
usuarios_ml = [65,15,56,72]

usuarios = []
usuarios.extend(usuarios_ds)
usuarios.extend(usuarios_ml)

#Forma correcta
usuarios = usuarios_ds.copy()
usuarios.extend(usuarios_ml)


usuarios = set(usuarios)


set(usuarios_ds) | set(usuarios_ml)

set(usuarios_ds) & set(usuarios_ml)

usuarios_sin_ml = set(usuarios_ds) - set(usuarios_ml)
usuarios_sin_ml

#usuarios que hicerion ml pero no ds
set(usuarios_ds) ^ set(usuarios_ml)


#Creacion de conjuntos
usuarios = {1,5,32,68,78,99,37}

25 in usuarios


frecuencias = {
    'Alvaro': 2,
    'encanta': 2,
    'me': 1,
    '2':1,
}

frecuencias.get('gusta',0)

frecuencias['Carlos'] = 5
frecuencias

#defaultdic
