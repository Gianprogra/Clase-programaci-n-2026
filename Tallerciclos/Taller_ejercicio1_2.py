# Todos los números positivos que son divisibles por 10 y menores que n. Por ejemplo, si el
# usuario ingresa un valor de 100, imprimiría 10 20 30 40 50 60 70 80 90

n = int(input('Ingrese un número: '))

i = 10

while i < n:
     i = i+10
     print(i)