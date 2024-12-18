
################### EJERCICIOS DE MANEJO DE FICHEROS #####################

################### EJERCICIO 1 #####################

# Crea un script que lea el archivo "contar_palabras.txt" de la carpeta "ficheros" y cuente la cantidad de palabras en él. 
# Puedes utilizar el método split() para separar las palabras en una lista y luego utilizar la función len() para contar el número de elementos en la lista.
  
nombre_fichero : str = './01.Ficheros y excepciones/ejercicios/ejercicios_ficheros/ficheros/contar_palabras.txt'

with open(nombre_fichero) as fichero_abierto:
    contenido : str = fichero_abierto.read()
    print(contenido)
    contenido_parseado : str = contenido.replace('\n', ' ')
    palabras : list = contenido_parseado.split(' ')
    print(palabras)
    cantidad_palabras : int = len(palabras)
    print(cantidad_palabras)

################### EJERCICIO 2 #####################

# Crea un script que lea el archivo de texto "palabras_repetidas.txt de la carpeta "ficheros" y cuenta la cantidad de veces que aparece una palabra específica en él. 
# Puedes utilizar el método count() para contar la cantidad de veces que aparece una palabra en una cadena de texto, imprimer el número.
# Reemplaza esta palabra repetida con el método "replace" y vuelve a escribir el texto en otro fichero llamado "palabras_sin_repetir.txt" .

fichero_fuente : str = './01.Ficheros y excepciones/ejercicios/ejercicios_ficheros/ficheros/palabras_repetidas.txt'
fichero_destino : str = './01.Ficheros y excepciones/ejercicios/ejercicios_ficheros/ficheros/palabras_sin_repetir.txt'


with open(fichero_fuente) as fichero_abierto:
    contenido : str = fichero_abierto.read()
    print(contenido)
    contenido_parseado : str = contenido.replace('\n', ' ')
    palabras : list = contenido_parseado.split(' ')
    cantidad_palabras_repetidas : int = palabras.count('palabras')
    print(f"La palabra palabras se repite {cantidad_palabras_repetidas} veces.")
    contenido_sin_repetidas : str = contenido.replace('palabras', '')

with open(fichero_destino, 'w') as fichero_abierto:
    fichero_abierto.write(contenido_sin_repetidas)

################### EJERCICIO 3 #####################

# Crea un script que tome una lista de números y los escriba en un archivo de texto llamado "numeros.txt", uno por línea. 
# Luego, crea otro script que lea ese archivo y sume los números e imprima el resultado por pantalla.
# Puedes utilizar el método write() para escribir en un archivo y el método read() para leer su contenido.

################### EJERCICIO EXTRA 1 #####################

# Crea un script que tome coja las imagenes de la carpeta "imagenes" y los copie en otra carpeta con el nombre "imagenes_procesadas". 
# Puedes utilizar el módulo "os" para crear la carpeta "imagenes_procesadas" con la función "os.makedirs(ruta)"
# Utiliza el módulo "os" también para listar las imagénes de la carpeta "imagenes" con la función "os.listdir(ruta)"
# Utiliza el módulo "shutil" para copiar cada imagen a la nueva carpeta "imagenes_procesadas" con la función "shutil.copy(ruta_origen,ruta_destino)"

################### EJERCICIO EXTRA 2 #####################

# Crea un script que lea el archivo "presupuestos.csv" CSV (comma-separated values) y lo almacene en una lista de diccionarios con el método "DictReader" de la librería "csv", 
# donde cada diccionario representa una fila del archivo y las claves son los nombres de las columnas.

