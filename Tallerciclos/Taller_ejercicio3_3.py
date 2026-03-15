# La suma de todos los dígitos impares de una entrada.

n = input('Ingrese un numero n:  ')

suma = 0 

for i in n:
    entero = int(i)
    if entero % 2 != 0:
        suma = suma + entero

print('La suma de los digitos es ---->', suma) 