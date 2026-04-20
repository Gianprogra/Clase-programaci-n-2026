# Usando la calculadora que se realizó en clase, implemente:
# Las funciones ya realizadas (Suma, Resta, Multiplicación, División y operación)
# Agregar una función que haga la raíz cuadrada, y el exponente, donde deben de depender de la fusión de la multiplicación.
# Agregar una función que implemente el factorial
# Agregar una función que realice la inversa de un número. (ejemplo: 2 la inversa es 1/2).



# No se usa lista ni diccionario porque solo trabajamos con valores individuales (a y b)

#  VARIABLES DE PRUEBA (a y b)
a = int(input('Ingrese un número para a: '))
b = int(input('Ingrese un número para b: '))


def suma(a, b):
    return a + b  # suma dos números

def resta(a, b):
    return a - b  # resta dos números

def multiplicacion(a, b):
    return a * b  # multiplica

def division(a, b):
    if b == 0:
        return "Error"  # evita división por cero
    return a / b

def raiz_cuadrada(a):
    return a ** 0.5  # calcula raíz de un número

def potencia(base, exponente):
    resultado = 1
    for i in range(exponente):  # repite multiplicación
        resultado *= base
    return resultado

def factorial(a):
    resultado = 1
    for i in range(1, a + 1):  # multiplica desde 1 hasta a
        resultado *= i
    return resultado

def inversa(a):
    if a == 0:
        return 'No existe'
    return 1 / a  # inverso del número



#  USO DE LAS FUNCIONES
print('Suma:', suma(a, b))
print('Resta:', resta(a, b))
print('Multiplicación:', multiplicacion(a, b))
print('División:', division(a, b))
print('Raíz de a:', raiz_cuadrada(a))
print('Potencia a^b:', potencia(a, b))
print('Factorial de a:', factorial(a))
print('Inversa de a:', inversa(a))