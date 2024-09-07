############################## ¿QUÉ SON LAS EXCEPCIONES? #####################################

# Las excepciones son una forma de manejar errores y problemas inesperados que pueden ocurrir durante 
# la ejecución de un programa. 

# Al utilizar excepciones, puede escribir código para detectar y responder a estos problemas de manera 
# más eficiente y organizada que si simplemente se permitiera que el programa 
# se detuviera o generara resultados incorrectos.

# Cuando ocurre un error o un problema inesperado durante la ejecución de un programa, 
# se dice que se ha "lanzado una excepción". La forma en que se maneja la excepción depende de 
# cómo se haya escrito el código. 
# 
# Por ejemplo, se puede escribir código para "atrapar" la excepción 
# y tomar medidas para solucionar el problema, o se puede escribir código para "lanzar" 
# la excepción a otra parte del programa que sabe cómo manejarla.

# En resumen, las excepciones son una herramienta útil para manejar errores y problemas inesperados 
# en un programa de manera organizada y controlada.

############################## EXCEPCIONES MÁS COMUNES EN PYTHON POR DEFECTO #####################################

# En Python, hay varias excepciones incorporadas que se pueden utilizar para manejar errores y problemas inesperados.
#  Algunas de las excepciones más comunes y útiles son:

# ValueError: se lanza cuando se proporciona un valor inapropiado para una función o una operación. 
# Por ejemplo, si intenta convertir una cadena a un número entero y la cadena 
# no tiene un formato válido para un número entero, se lanzará un ValueError.

# TypeError: se lanza cuando se realiza una operación o se llama a una función con un tipo de datos inapropiado. 
# Por ejemplo, si intenta concatenar una 
# cadena y un número con el operador +, se lanzará un TypeError.

# KeyError: se lanza cuando se intenta acceder a un elemento de un diccionario utilizando una clave que 
# no existe en el diccionario.

# IndexError: se lanza cuando se intenta acceder a un índice fuera de los límites de una lista o una cadena.

# IOError: se lanza cuando se produce un error al intentar leer o escribir un archivo.

# ImportError: se lanza cuando se produce un error al importar un módulo o un paquete.


############################## SINTAXIS #####################################
# try:
#       codigo que puede provocar excepcion en tiempo de ejecucion.
# except NombreExcepcion:
#       codigo que maneje la excepcion cuando ocurra.

 
############################## EXCEPCIÓN CUANDO UN FICHERO NO EXISTE #####################################

# La excepción FileNotFoundError ya viene definida por defecto en Python.



############################## EXCEPCIONES PERSONALIZADAS SIN CONSTRUCTOR #####################################

# Estas excepciones las lanzamos cuando solo queremos ver un mensaje, sin un comportamiento muy avanzado, 
# como podría ser escribir en un fichero de log el fallo.

    
############################## EXCEPCIONES PERSONALIZADAS CON CONSTRUCTOR #####################################


# Aquí, hemos sobreescrito el constructor de la clase Exception para aceptar nuestros propios argumentos 
# personalizados salario y mensaje. 
# 
# Entonces, el constructor de la clase 
# se llama manualmente con el argumento self.message utilizando super().
# El atributo personalizado self.salary se define para ser utilizado posteriormente.
# El método heredado __str__ de la clase Exception se utiliza para mostrar el mensaje correspondiente 
# cuando se produce el error SalaryNotInRangeError.
# También podemos personalizar el propio método __str__ sobreescribiendolo.
