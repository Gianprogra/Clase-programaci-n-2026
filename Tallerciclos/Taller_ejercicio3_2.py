# La suma de todos los números impares comprendidos entre a y b (ambos inclusive), donde 
# a y b son entradas.

a = int(input('Ingrese el primer número: '))
b = int(input('Ingrese el segundo número: '))

suma = 0

for i in range (a,b+1):
    if i % 2 != 0:
        suma = suma + i

print('La suma de los impares entre',a,'y',b,'es',suma)