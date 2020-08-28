def add_time(inicio, duracion, dia=None):
    h1 = int(inicio.split(':')[0])
    m1 = int(inicio.split(':')[1].split()[0])
    periodo = inicio.split(':')[1].split()[1]
    h2 = int(duracion.split(':')[0])
    m2 = int(duracion.split(':')[1].split()[0])

    hora_fin = h1 + h2
    minutos_fin = m1 + m2

    while minutos_fin >=60:
        minutos_fin -= 60
        hora_fin += 1

    while hora_fin >= 12:
        hora_fin -= 12
        if periodo == 'AM':
            periodo = 'PM'
        else:
            periodo = 'AM'

    if dia is None:
        print("{}:{:02d} {}".format(hora_fin, minutos_fin, periodo))
    else:
        print("{}:{:02d} {}, {}".format(hora_fin, minutos_fin, periodo, dia.capitalize()))

    
add_time("3:00 PM", "3:10")
# Returns: 6:10 PM
 
add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday
 
add_time("11:43 AM", "00:20")
# Returns: 12:03 PM