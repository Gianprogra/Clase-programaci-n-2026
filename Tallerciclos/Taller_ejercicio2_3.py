# La suma de todos los números impares entre a y b (ambos inclusive).

a = int(input('Ingrese el número (a): '))
b = int(input('Ingrese el número (b): '))

suma = 0
i = a
while i <= b:
    if i % 2 != 0:
        suma = suma + i
    i = i + 1

print(suma)
