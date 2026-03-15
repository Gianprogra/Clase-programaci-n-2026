# La suma de todos los dígitos impares de n. (Por ejemplo, si n es 32677, la suma sería 3 + 7
# + 7 = 17.)

n = int(input('Ingrese un número (n): '))

suma = 0 

while n > 0:
    digt = n % 10
    if digt % 2  != 0:
        suma = suma + digt
    
    n = n // 10

print('La suma de los digitos es ---->', suma)

