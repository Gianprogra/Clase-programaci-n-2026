
# Escribe un programa que reciba una lista de temperaturas (°C) de un día tomadas cada ho-ra: 24 horas (la lista la debe de implementar usted mismo) y que permita:
# Calcular la temperatura promedio.
# Determinar la temperatura más alta y más baja.
# Contar cuántas veces estuvo por encima del promedio.



temperaturas = [20, 21, 19, 18, 22, 24, 25, 26, 27, 28, 29, 30,
                31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20] # Se utiliza  una lista tipo (list) para acceder por orden y indice

def promedio(listas):
    return sum(listas) / len(listas) # suma todos los valores y divide entre la cantidad

def Laterales(listas): # Se usa lista porque necesitamos recorrer valores para encontrar extremos
    return max(listas), min(listas) # devuelve el mayor y menor valor

def sobre_promedio(lista): # Se utiliza lista porque se recorre con un ciclo
    
    prom = promedio(lista)
    contador = 0
    
    for temp in lista:  # recorre cada temperatura
        if temp > prom:  # verifica si está por encima del promedio
            contador += 1
    
    return contador

print(promedio(temperaturas))
print(Laterales(temperaturas))
print(sobre_promedio(temperaturas))
    