# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese dos palabras y arme combinaciones con ella
print('Ingrese palabra 1:')
palabra_1 = str(input())

print('Ingrese palabra 2:')
palabra_2 = str(input())

# De la primera palabra tome las primeras tres letras, utilice el operador :
pal1 = palabra_1[0:3]
# De la segunda palabra tome las primeras dos letras, utilice el operador :
pal2 = palabra_2[0:2]
# Formar una nueva palabra con los recortes solicitados
nuevapalabra = pal1 + pal2
# Imprima en pantalla los resultados
print("La nueva palabra es: ", nuevapalabra)
