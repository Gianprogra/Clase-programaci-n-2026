# Crear una máquina dispensadora la cual pueda: 
# Se usa un DICCIONARIO porque cada producto tiene un precio asociado
productos = {
    'gaseosa': 3000,
    'papas': 2500,
    'agua': 1500
}

def comprar():
    producto = input('Producto: ')  # lee el producto que quiere el usuario
    
    if producto not in productos:   # verifica si el producto existe
        print('No existe')
        return                      # termina la función si no existe
    
    precio = productos[producto]    # obtiene el precio según la clave
    
    dinero = int(input('Dinero: ')) # convierte el dinero ingresado a entero
    
    if dinero < precio:             # compara si el dinero alcanza
        print('Falta dinero')
    else:
        cambio = dinero - precio    # calcula el cambio
        print('Cambio:', cambio)

comprar()                           # ejecuta la función