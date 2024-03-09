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
