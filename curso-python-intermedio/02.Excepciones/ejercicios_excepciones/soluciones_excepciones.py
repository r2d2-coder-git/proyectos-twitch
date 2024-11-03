################### EJERCICIOS DE EXCEPCIONES #####################


################### EJERCICIO 1 #####################

# Crea una clase "CuentaBancaria" que represente una cuenta bancaria con un saldo y un límite de extracción. 
# Agrega un método "extraer" que permita al usuario retirar dinero de la cuenta. 
# Si el usuario intenta extraer más dinero del que tiene disponible en la cuenta (incluyendo el límite de extracción), 
# lanza una excepción "SaldoInsuficiente" con un mensaje que indique al usuario que no tiene suficientes fondos 
# para realizar la transacción.

class SaldoInsuficiente(Exception):
    pass

class CuentaBancaria:
    __saldo : int 
    __limite_extraccion : int 

    def __init__(self, saldo : int, limite_extraccion : int) -> None:
        self.__saldo = saldo
        self.__limite_extraccion = limite_extraccion
    
    def extraer(self, cantidad : int) -> None:
        if cantidad > self.__saldo or cantidad > self.__limite_extraccion:
            raise SaldoInsuficiente("No tienes suficientes fondos o has superado el limite diario.")
        
        self.__saldo -= cantidad
        print(f"Se extrajeron {cantidad} de euros. Saldo restante: {self.__saldo}")

cuenta : CuentaBancaria = CuentaBancaria(1000, 300)

try: 
    cantidad_a_extraer : int = int(input('Cuanto dinero quieres sacar de la cuenta? '))
    cuenta.extraer(cantidad_a_extraer)
except ValueError: 
    print("Ingrese un valor númerico válido")
except SaldoInsuficiente as e:
    print(e)


################### EJERCICIO 2 #####################

# Crea una función "validar_edad" que reciba una edad y valide que sea un número entero y mayor a 0. 
# Si no cumple con estas condiciones, lanza una excepción "EdadInvalida" con un mensaje que indique 
# al usuario que la edad ingresada no es válida. Utiliza esta función en otra función "registro" que 
# reciba un nombre y una edad y valide que la edad ingresada sea válida antes de registrar al usuario.

class EdadInvalida(Exception):
    pass

def validad_edad(edad : int) -> None:
    if not isinstance(edad, int) or edad <= 0:
        raise EdadInvalida("La edad que tienes no es válida. (Debe ser un número entero mayor que 0).")

    return None

def registro(nombre: str, edad : int) -> bool:
    try:
        validad_edad(edad)
        print(f"Usuario registrado -> Nombre: {nombre}, Edad: {edad}")
    except EdadInvalida as e:
        print(e)

nombre : str = input("Dame tu nombre: ")

try: 
    edad : int  = int(input("Dame ahora tu edad: "))
    registro(nombre, edad)
except ValueError: 
    print("La edad debe ser un número entero.")