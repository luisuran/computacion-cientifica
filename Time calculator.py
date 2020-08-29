def add_time(inicio, duracion, dia=None):
    h1 = int(inicio.split(':')[0])
    m1 = int(inicio.split(':')[1].split()[0])
    periodo = inicio.split(':')[1].split()[1]
    h2 = int(duracion.split(':')[0])
    m2 = int(duracion.split(':')[1].split()[0])

    hora_fin = h1 + h2
    minutos_fin = m1 + m2

    dias = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    canti_dias = 0

    # Calculo la cantidad de horas y minutos finales
    while minutos_fin >= 60:
        minutos_fin -= 60
        hora_fin += 1

    # Calculo el período final
    while hora_fin >= 12:
        hora_fin -= 12
        if periodo == 'AM':
            periodo = 'PM'
        else:
            periodo = 'AM'
            canti_dias += 1     # Cuento la cantidad de días

    if hora_fin == 0: hora_fin = 12

    respuesta = "{}:{:02d} {}".format(hora_fin, minutos_fin, periodo)

    if dia is not None:
        # Calculo la posición en el arreglo de días
        pos_inicial = dias.index(dia.capitalize())
        pos = pos_inicial + canti_dias

        # Si la posición es mayor al tamaño del arreglo voy restando hasta hacerlo entrar
        while pos > 6:
            pos -= 7
        respuesta += ", {}".format(dias[pos])

    if canti_dias == 1:
        respuesta += " (next day)"

    if canti_dias > 1:
        respuesta += " ({} days later)".format(canti_dias)
    
    print(respuesta)


add_time("3:00 PM", "3:10")
# Returns: 6:10 PM
 
add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday
 
add_time("11:43 AM", "00:20")
# Returns: 12:03 PM
 
add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)
 
add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)
 
add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)