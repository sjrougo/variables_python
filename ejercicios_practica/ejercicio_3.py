# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese primero su nombre y luego su apellido
# Capture ambos datos e imprima su nombre completo
print('Ingrese por consola su nombre/s:')
nombre = str(input())

print('Ingrese por consola su apellido/s:')
apellido = str(input())

# Imprima su nombre completo
print("El nombre completo es: ", nombre, apellido)
# Almacenar su nombre completo en una variable
# nombre_completo = .....
ncompleto = nombre + " " + apellido #Se agrega espacio en blanco para prolijidad

# Imprimir la cantidad de letras que posee su nombre completo
# cantidad_letras = len(....)
cantidad_letras = len(ncompleto) - 1
# En línea se cuenta la cant de caracteres, restando 1 teniendo en cuenta el espacio agregado en línea 24
print("La cantidad de letras que posee su nombre completo es: ", cantidad_letras)
