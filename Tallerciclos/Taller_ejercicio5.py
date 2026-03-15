# Un tanque de agua tiene dos detectores: uno de tanque lleno y otro de tanque vacío. Una per-
#V sona extrae continuamente agua del tanque. Un sistema automático abre la válvula de entrada de
# agua si el detector de tanque vacío se activa. La válvula permanece abierta hasta que el detector
# de tanque lleno se activa. En ese momento se debe cerrar la válvula.

valvula = 0 

while True:
    sensor_vacio = int(input('Sensor de vacío (0 o 1): '))
    sensor_llenado = int(input('Sensor de llenado (0 o 1): '))
    
    if sensor_vacio == 1:
        valvula = 1
    
    if sensor_llenado == 1:
        valvula = 0
    print('Estado de la valvula: ', valvula)
    
    break
