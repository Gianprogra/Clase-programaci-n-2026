# ejercicio  6 
# 1 es suma 
# 2 es resta 
# 3 es multiplicación
# 4 es división

eleccion = input('Ingrese la operacion que desea hacer: ')

if eleccion == "+" :
    print('(se escogio suma)')
    a = int(input('Ingrese el número 1: '))
    b = int(input('Ingrese el número 2: '))
    
    total = a + b 
    
    print('(La suma dio): ',total)
elif eleccion == "-":
    print('(Se escogio resta)')
    a = int(input('Ingrese el número 1: '))
    b = int(input('Ingrese el número 2: '))
    
    total = a - b
    
    print('(La resta dio): ', total)
elif eleccion == "*":
    print('(Se escogió multiplicación)')
    a = int(input('Ingrese el número 1: '))
    b = int(input('Ingrese el número 2: '))
    
    total = a * b
    
    print('(La multiplicación): ', total)
elif eleccion == "/":
    print('(Se escogio división)')
    a = int(input('Ingrese el número 1: '))
    b = int(input('Ingrese el número 2: '))
    
    total = a/b 
    
    print('(La divisón dio): ', total)
else:
    print('Opción incorrecta')