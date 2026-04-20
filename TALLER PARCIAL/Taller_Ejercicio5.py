# Crea un juego donde el usuario deba adivinar un número secreto entre 1 y 100. El programa debe:
# Pedir el nivel de dificultad (Fácil, Medio, Difícil).
# Generar un número aleatorio.
# Dar pistas si el número es mayor o menor.
# Mostrar cuántos intentos quedan.






import random # permite generar números aleatorios.

def elegir_dificultad():
    nivel = input('Nivel: ')  # lee el nivel escrito por el usuario
    
    if nivel == 'facil':
        return 10             # fácil da 10 intentos
    elif nivel == 'medio':
        return 7              # medio da 7 intentos
    else:
        return 5              # difícil da 5 intentos

def generar_numero():
    return random.randint(1, 100)  # genera un número entre 1 y 100

def jugar(intentos):
    numero = generar_numero()      # guarda el número secreto
    
    while intentos > 0:            # repite mientras queden intentos
        intento = int(input('Número: '))  # convierte lo escrito a entero
        
        if intento == numero:
            print('Ganaste')       # el usuario acertó
            return                 # termina la función
        
        elif intento < numero:
            print('Mayor')         # el número secreto es mayor
        else:
            print('Menor')         # el número secreto es menor
        
        intentos -= 1              # descuenta un intento

jugar(elegir_dificultad())         # inicia el juego pidiendo la dificultad