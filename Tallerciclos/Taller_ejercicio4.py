# Si en un reloj digital registra las 6 AM, hacer sonar una alarma por 1 minuto a menos que se
# accione el botón de apagado.

Hora = 6
Minuto = 0

print('Son las 6:00 AM. ¡Se activa la alarma!')

while Minuto < 6:
    print('La alarma suena un minuto', Minuto + 1)
    
    opcion = input('Escriba "off" para apagar la alarma: ')
    if opcion.lower() == 'off':
        print('Se apago la alarma')
        break
    Minuto = Minuto + 1
    
if  Minuto == 6:
    print( 'La alarma se apago despues de un minuto') # pongo 6 porque 60 veces para es mucho jaja
    