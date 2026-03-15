# Semáforo 

Boton = input('Luz roja: ')

if Boton == 'rojo' or Boton == 'Rojo':
    print('Se enciende por 20s')

    Boton2 = input('Siguiente luz: ')

    if Boton2 == 'verde' or Boton2 == 'Verde':
        print('Se enciende por 40s')

        Boton3 = input('Siguiente luz: ')

        if Boton3 == 'amarillo' or Boton3 == 'Amarillo':
            print('Se enciende junto con verde por 5s')
            print('Se apagan verde y amarillo')
        else:
            print('Luz no válida')

    else:
        print('Luz no válida')

else:
    print('Luz inicial incorrecta')