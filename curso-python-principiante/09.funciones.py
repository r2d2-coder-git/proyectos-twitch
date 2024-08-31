from typing import Union

# Sintaxis: def nombre_funcion(parametro1 : Tipo1, parametro2: Tipo2) -> TipoDatoRetorno:
#               Acciones
#               return Valor (Opcional)

############################# FUNCIÓN SIN PARÁMETROS #####################################

def funcion_basica() -> None:
    print("Uso de funcion basica")
    return

############################# FUNCIÓN CON PARÁMETROS #####################################

# Python es un lenguaje con tipado dinámico, es decir, no hace falta indicar que tipo de datos va a recibir o devolver una función
# Es muy recomendable indicar los tipos de datos para aumentar la legibilidad del código.
# Es más, aunque tu le indiques el tipo de parámetros y luego le pasas otro tipo de datos NO va a dar un fallo.

def suma(numero1: int, numero2: int) -> int:
    resultado : int = numero1 + numero2
    return resultado

cadena1 : str = "hola"
cadena2 : str = "adios"

resultado_suma : int = suma(10, 20)
print(resultado_suma)

############################# FUNCIÓN CON PARÁMETROS CON VALORES POR DEFECTO #####################################

def sacar_dinero(dinero_cuenta : int, dinero_a_retirar : int = 50) -> int: 
    return dinero_cuenta - dinero_a_retirar

mi_dinero : int = 5000

cuenta_actual : int = sacar_dinero(dinero_a_retirar=1000, dinero_cuenta=mi_dinero)

print(cuenta_actual)

############################# FUNCIÓN CON PARÁMETROS OPCIONALES #####################################

# En los parametros opcionales no hace falta definir que tipo de datos tienen porque internamente python los va a meter en tuplas. Los toppings que

def crear_pizza(tipo_pizza : str, *toppings_extra) -> str:
    tipos_pizza : list = ['margarita', 'cuatro quesos', 'barbacoa']
    frase_respuesta : str = ""

    if tipo_pizza in tipos_pizza and not toppings_extra:
        frase_respuesta = f"Tu pizza {tipo_pizza} se está procesando vuelve en 5 minutos."
    elif tipo_pizza in tipos_pizza and toppings_extra:
        frase_respuesta = f"Tu pizza {tipo_pizza} con los toppings {str(toppings_extra)} se está procesando vuelve en 5 minutos."
    else:
        frase_respuesta = f"El tipo de pizza que has elegido no lo hacemos en nuestra máquina."

    return frase_respuesta

respuesta1 = crear_pizza('diavola')

print(respuesta1)

# Salchicha y pimiento rojo son parámetros opcionales.

############################# FUNCIÓN CON PARÁMETROS KEY-VALUE #####################################

# Sirve para cuando necesitamos un número variable de parámetros que tengan forma de diccionario, el nombre kwargs se pone por convención del lenguaje.
# En este caso queremos crear un perfil de usuario que tenga como obligatorio poner el nombre y apellidos y la demás información de forma opcional.

def crear_perfil_usuario(nombre: str, apellido: str, **kwargs) -> str:
    perfil = f'**************************** INFORMACIÓN DEL USUARIO {nombre} {apellido} *****************************'
    for key, value in kwargs.items():
        perfil = f'{perfil}\n {key} : {value}'

    return perfil

perfil_formateado: str = crear_perfil_usuario(nombre='arturo', 
                                              apellido='lorenzo', 
                                              telefono=103480348, 
                                              hobbie='gimnasio', 
                                              dni='djfaljfa')

print(perfil_formateado)



############################# FUNCIÓNES QUE TIENEN COMO PARÁMETROS FUNCIONES #####################################

# Todo en Python son objetos hasta las funciones por eso podemos pasar una función como parámetro a otra función.
# En este ejemplo hacemos una función que reciba que tipo de operación tiene que hacer sobre dos números, está operación se define como una función.

def sumar(x : int, y: int) -> int:
    return x + y 

def calculadora(operacion, x : int , y: int) -> int:
    return operacion(x, y)

print(calculadora(sumar, 1, 2))

############################# FUNCIÓNES QUE DEVUELVE MÁS DE UN VALOR #####################################
        
def dos_elementos(lista : list) -> Union[str, str]:
    if len(lista) >= 2: 
        return lista[0], lista[1]
    
    return "","" 

nombres = ['Arturo', 'Pepe', 'Maria']

nombre1, nombre2 = dos_elementos(nombres)

print(nombre1)
print(nombre2)

############################# ORDEN DE PARÁMETROS #####################################

# Orden de posicionamiento de los parámetros según el tipo:
# 1. Parametros obligatorios
# 2. Parametros opcionales
# 3. Parametros key-value.
#        def funcion(parametros_obligatorios, *parametros_opcionales, **kwargs_arguments)