from datetime import datetime, timedelta, date

# Obtener la fecha y hora actuales
ahora : datetime = datetime.now()
print(ahora)

# Formatear la fecha y la hora en un formato específico
fecha_formateada : str = ahora.strftime("%d/%m/%Y %H:%M:%S")
print(fecha_formateada)
print(type(fecha_formateada))

# Parsear una cadena a un objeto datetime
fecha_str : str = "01/09/2024 15:30:00"
fecha_parsed : datetime = datetime.strptime(fecha_str, "%d/%m/%Y %H:%M:%S")
print(fecha_parsed)
print(type(fecha_parsed))

# Realizar operaciones con fechas
# Agregar 7 días a la fecha actual
fecha_futura : datetime = ahora + timedelta(days=7)
print(fecha_futura)

# Restar 3 días a la fecha actual
fecha_pasada : datetime = ahora - timedelta(days=3)
print(fecha_pasada)

# Calcular la diferencia entre dos fechas
diferencia : timedelta = ahora - fecha_pasada
print(diferencia)
print(type(diferencia))
print(diferencia.days)

# Crear una fecha específica
fecha_especifica : datetime = datetime(2024, 9, 1, 15, 30, 0)

print(fecha_especifica)

# Obtener solo la fecha actual (sin hora)
fecha_solo : date = date.today()
print(fecha_solo)

# Obtener el primer y último día del mes actual
primer_dia_del_mes : date = fecha_solo.replace(day=1)
print(primer_dia_del_mes)

# Encontrar el día de la semana
dia_de_la_semana : str = ahora.strftime("%A")
print(dia_de_la_semana)

# Determinar si un año es bisiesto
def es_bisiesto(year):
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 ==0)

print(es_bisiesto(1034))

# Convertir un objeto datetime a un timestamp (segundos desde Epoch)
timestamp : float = ahora.timestamp()

print(timestamp)
# Convertir un timestamp a un objeto datetime
fecha_desde_timestamp : datetime = datetime.fromtimestamp(timestamp)
print(fecha_desde_timestamp)

# Comparar dos fechas
if fecha_pasada < ahora:
    print(f"La fecha pasada es anterior al ahora")


# Calcular la edad en años dada una fecha de nacimiento
fecha_nacimiento : datetime = datetime(1995, 11, 30)
edad = ahora.year - fecha_nacimiento.year - ((ahora.month, ahora.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
print(edad)

dia_actual_year = ahora.timetuple().tm_yday
print(dia_actual_year)