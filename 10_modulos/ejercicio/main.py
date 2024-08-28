################### EJERCICIO 1 #####################

# 1.Crea un archivo llamado "validaciones.py" y define una función llamada "validar_email" que reciba una cadena de texto como argumento y retorne verdadero 
#   si es una dirección de correo electrónico válida o falso en caso contrario, un correo es válido: 
#   si empieza por algo distinto al '@' y termina en '@gmail.com'.
# 2.Crea otro archivo llamado "registro.py" e importa el módulo "validaciones" con la sentencia "import validaciones"
# 3.Crea una función en el archivo "registro.py" llamada "registrar_usuario" que reciba un nombre y un correo electrónico como argumentos. 
#   3.1.Dentro de esta función, utiliza la función "validar_email" del módulo "validaciones" para verificar si el correo electrónico es válido. 
#   3.2.Si es válido, imprime "El usuario [nombre] ha sido registrado con el correo [correo electrónico]", de lo contrario imprime "El correo electrónico no es válido".
# 4.Crea un archivo llamado "main.py" e importa el módulo "registro" con la sentencia "import registro"
# 5.En el archivo "main.py" llama a la función "registrar_usuario" del módulo "registro" pasando un nombre y un correo electrónico como argumentos.

from registro import registrar_usuario

nombre = input('Escribe tu nombre... ')
correo = input('Escribe tu correo electronico... ')

registrar_usuario(nombre, correo)