# Un profesor guarda las notas de sus estudiantes en un diccionario:

# Crea funciones que permitan:
# Calcular el promedio simple de cada estudiante.
# Calcular un promedio ponderado (30 %, 30 %, 40 %).
# Determinar quién tiene el mayor promedio final.
# Mostrar solo los estudiantes aprobados (≥ 3.0).
# Mostrar mensaje el cual diga quien aprobó o no la clase de la profesora Mcgonagall

# Diccionario donde cada clave es un nombre y su valor es una lista de notas
notas = {
    'Harry': [3.8, 4.0, 4.2],
    'Ron': [3.2, 3.8, 2.8],
    'Hermione': [5.0, 5.0, 5.0]
}


def promedio_simple(lista): # Recibe una lista de notas y calcula el promedio sumando todo y dividiendo
    return sum(lista) / len(lista)  # sum() suma todos, len() cuenta cuántos hay


def promedio_ponderado(lista): # Calcula promedio donde cada nota tiene un peso diferente (30%, 30%, 40%)
    return lista[0]*0.3 + lista[1]*0.3 + lista[2]*0.4  # posición 0,1,2 = nota 1,2,3


def mejor_estudiante(dic): # Recorre el diccionario buscando quién tiene el mayor promedio ponderado
    mejor = ""    # guardará el nombre del ganador
    mayor = 0     # guardará el promedio más alto encontrado
    
    for estudiante in dic:                        # recorre cada nombre del diccionario
        prom = promedio_ponderado(dic[estudiante])# calcula su promedio ponderado
        
        if prom > mayor:   # si este promedio supera al mayor registrado
            mayor = prom   # actualiza el mayor
            mejor = estudiante  # actualiza quién es el mejor
    
    return mejor  # devuelve el nombre del mejor estudiante


def aprobados(dic): # Recorre el diccionario e indica si cada estudiante aprobó o reprobó
    for estudiante in dic:
        if promedio_ponderado(dic[estudiante]) >= 3.0:  # nota mínima para aprobar
            print(estudiante, 'obtuvo calificación suficiente')  # aprobó
        else:
            print(estudiante, 'no alcanzó la nota mínima')  # reprobó


print('Mejor estudiante:', mejor_estudiante(notas)) # Imprime el nombre del estudiante con mayor promedio ponderado

 
aprobados(notas) # Muestra el estado de cada estudiante