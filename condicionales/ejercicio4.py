# Llenado de tanques 

# 1 sensor activo
# 0 sensor inactivo

Sensor_vacio = int(input('¿Sensor de vacío activo?: '))
Sensor_lleno = int(input('¿Sensor de lleno activo?: '))

if Sensor_vacio == 1:
    print("Se abre la válvula de entrada de agua.")

    if Sensor_lleno == 1:
        print('El tanque está lleno')
        print('Se cierra la válvula')
    else:
        print('La válvula permanece abierta hasta que el tanque se llene')

else:
    print('El tanque no está vacío. La válvula permanece cerrada')