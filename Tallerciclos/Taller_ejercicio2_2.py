# La suma de todos los cuadrados entre 1 y 100 (ambos inclusive).

suma = 0


for i in range(1,101,1):
    suma = suma + i**2

print(suma)