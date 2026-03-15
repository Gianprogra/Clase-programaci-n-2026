# Programa del reloj, para ue funcione el boton tiene que escribirlo 

Reloj = int(input('Ingrese la hora: '))
Boton = input('Presione el boton de apagado (Y/N)')

if Reloj == 6:
    print('Suena alarma por (un minuto)')
    if Boton == 'Y':
        print('Se apago la alarma')
    else:
        print('No se apago la alarma')