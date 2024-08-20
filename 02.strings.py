# En Python, un string es una secuencia de caracteres. Pueden ser números, letras, símbolos, y cualquier otro carácter que puedas imaginar. 
# Se representan con comillas simples ('') o comillas dobles ("").

# Los strings se utilizan para representar texto o información alfanumérica en un programa. Pueden ser manipulados y concatenados 
# con otros strings y números utilizando operadores matemáticos y especiales de concatenación.


################### FUNCIONES MÁS UTILIZADAS #####################

# len(string): Devuelve la longitud de un string.

# str.strip(): Devuelve un string sin espacios en blanco al principio o al final.

# str.replace(old, new): Reemplaza una parte de un string con otra.

# str.lower(): Convierte todos los caracteres de un string a minúsculas.

# str.upper(): Convierte todos los caracteres de un string a mayúsculas.

# str.title(): Convierte el primer carácter de cada palabra en un string a mayúsculas.

# str.startswith(prefijo): Devuelve True si el string comienza con el prefijo especificado.

# str.endswith(sufijo): Devuelve True si el string termina con el sufijo especificado.

# str.find(sub): Devuelve la posición del primer carácter de la primera aparición del string sub en el string original.


# 1. Longitud de un string
saludo : str = "Hola me llamo Arturo"
#print(dir(saludo))
longitud : int = len(saludo)
print(longitud)


# 2. Quitar espacios en blanco de al principio y final de un string
string_espacios : str = "                Esto es un string con espacios feos                      "
string_sin_espacios : str = string_espacios.strip()
print(string_sin_espacios)

# 3. Reemplazar partes de un string por otro.
mensaje_cifrado : str = "PEESTOPEESPEUNPEMENSAJEPECIFRADOPE"
mensaje_sin_cifrar : str = mensaje_cifrado.replace('PE', ' ').strip()

print(mensaje_sin_cifrar)

# 4. Poner un string en minusculas o mayusculas

minuscula : str = 'vamos a gritar un poco'
grito : str = minuscula.upper()

mayusculas : str = 'HABLEMOS UN POCO BAJITO'
susurro : str = mayusculas.lower()
print(susurro)

# 5. Comprobar si un string tiene prefijos o sufijos.
url : str = "www.r2d2.com"

prefijo : bool = url.startswith("www")
sufijo : bool = url.endswith(".com")

print(sufijo)

# 6. Encontrar la posición del primer carácter de la primera aparición del string sub en el string original, si no lo encuentra devuelve -1.

indice : int =  url.find("r2d2")
print(indice)

# 7. Concatenación de strings y f-strings.
nombre : str = "Arturo"
edad : int = 25
cargo : str = "Ingeniero informatico"


saludo : str = "Mi nombre es " + nombre + " tengo una edad de " + str(edad) + " años" + " y soy " + cargo
saludo_f_str = f"Mi nombre es {nombre} tengo una edad de {str(edad)} años y soy {cargo}"

print(saludo)
print(saludo_f_str)

strings_iguales = saludo == saludo_f_str
print(strings_iguales)