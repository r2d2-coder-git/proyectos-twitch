from datetime import datetime, timedelta
import pytz

# Obtener la fecha y hora actuales en UTC
utc_now = datetime.now(pytz.utc)

print(utc_now)
# Definir la zona horaria para Nueva York y Tokio
tz_ny = pytz.timezone('America/New_York')
tz_tokyo = pytz.timezone('Asia/Tokyo')

# Convertir la hora actual en UTC a las zonas horarias especificadas
ny_time = utc_now.astimezone(tz_ny)
tokyo_time = utc_now.astimezone(tz_tokyo)
print(tokyo_time)
print(ny_time)

# Crear un objeto datetime en una zona horaria específica
dt_ny = tz_ny.localize(datetime(2024, 9, 1, 15, 30, 0))

print(dt_ny)

# Convertir una hora en una zona horaria específica a UTC
dt_ny_utc = dt_ny.astimezone(pytz.utc)

print(dt_ny_utc)

# Calcular la diferencia entre dos zonas horarias
print(ny_time)
print(tokyo_time)
diff = tokyo_time.utcoffset() - ny_time.utcoffset()
print(diff)

# Obtener la información sobre la zona horaria actual
print(tz_ny)
print(tz_tokyo)

# Manejar la conversión entre una hora en una zona horaria y otra
dt_tokyo_converted = dt_ny.astimezone(tz_tokyo)
print(dt_tokyo_converted)