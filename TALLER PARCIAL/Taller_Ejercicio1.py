
# Escribe un programa que reciba una lista de temperaturas (°C) de un día tomadas cada ho-ra: 24 horas (la lista la debe de implementar usted mismo) y que permita:
# Calcular la temperatura promedio.
# Determinar la temperatura más alta y más baja.
# Contar cuántas veces estuvo por encima del promedio.



temperaturas = [20, 21, 19, 18, 22, 24, 25, 26, 27, 28, 29, 30,
                31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20]

def promedio(listas):
    return sum(listas) / len(listas)

def Laterales(listas):
    return max(listas), min(listas)

def sobre_promedio(lista):
    
    prom = promedio(lista)
    contador = 0
    
    for temp in lista:  # recorre cada temperatura
        if temp > prom:  # verifica si está por encima del promedio
            contador += 1
    
    return contador

print(promedio(temperaturas))
print(Laterales(temperaturas))
print(sobre_promedio(temperaturas))
    