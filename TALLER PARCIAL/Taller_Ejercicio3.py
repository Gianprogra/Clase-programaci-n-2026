# Diseña un sistema que gestione productos en un inventario.
# Cada producto tiene nombre, cantidad y precio. Usa un diccionario donde las claves sean los nombres.
# Implementa funciones para:
# agregar_producto(diccionario, nombre, cantidad, precio)
# eliminar_producto(diccionario, nombre)
# calcular_valor_total(diccionario)
# mostrar_inventario(diccionario)


# Se utiliza un DICCIONARIO porque se manejan productos con nombre (clave) y datos (valor)
inventario = {}

def agregar_producto(inv, nombre, cantidad, precio): # Diccionario porque permite relacionar nombre con cantidad y precio
    inv[nombre] = {'cantidad': cantidad, 'precio': precio}

def eliminar_producto(inv, nombre):
    if nombre in inv: # El if está para verificar que el producto existe antes de intentar eliminarlo.
        del inv[nombre]  # elimina el producto

def calcular_valor_total(inv):
    total = 0
    
    for producto in inv:  # recorre el diccionario
        total += inv[producto]['cantidad'] * inv[producto]['precio']
    
    return total

def mostrar_inventario(inv):
    for producto in inv:
        print(producto, inv[producto])  # muestra datos


agregar_producto(inventario, 'Arroz', 15, 2500)
agregar_producto(inventario, 'Leche', 50, 4300)
agregar_producto(inventario, 'Milo', 10 , 1200)
eliminar_producto(inventario,'Milo')

mostrar_inventario(inventario)
print('Valor total:', calcular_valor_total(inventario))

