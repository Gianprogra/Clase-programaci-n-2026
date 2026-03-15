# Todas las potencias de dos menores (2
# contador) que n. Por ejemplo, si el usuario ingresa un
# valor de n igual a 100, imprime 1 2 4 8 16 32 64.

n = int(input('Ingrese un número: '))

contador = 1

while 2**contador < n:
    respuesta = 2**contador
    print(respuesta)
    contador = contador + 1