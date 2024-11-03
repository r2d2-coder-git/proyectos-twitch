############################# FUNCIÓNES ANIDADAS #####################################

# Una función interna es simplemente una función que se define dentro de otra función. 
# La función interna puede acceder a las variables que se han
# definido dentro del alcance de la función externa, pero no puede cambiarlas.

# Hay varias razones por las que es posible que necesitemos crear una función interna:

# 1. Si queremos que la función anidada solo sea utilizada en el contexto de la función que la contiene, 
# entonces podemos usarla para encapsular
# una parte del código y hacerlo más legible.

# 2. Las funciones anidadas también pueden ser útiles para compartir una parte del código 
# entre varias funciones. En este caso,
# podemos definir la función anidada una vez y luego usarla desde varias funciones con decoradores.

# 3. Las funciones anidadas también pueden ser útiles para crear funciones "auxiliares" 
# que solo necesiten ser utilizadas en el contexto de otra
# función. En este caso, podemos definir la función anidada justo donde la necesitemos 
# y luego usarla para realizar una tarea específica dentro de la función que la contiene.

def funcion1(): 
    print("hola mundo desde la funcion principal")
    def funcion2():
        print("hola desde la funcion anidada")

    funcion2()

funcion1()

def fuera(x): 
    def dentro(y, z):
        return x + y + z
    
    return dentro

add_five = fuera(5)
resultado_final = add_five(5, 5)

print(resultado_final)
############################# DECORADORES SIN PARAMETROS #####################################

def funcion_decoradora(func):
    def funcion_interna():
        print("Soy una funcion interna y te han decorado pringado.")
        func()
    return funcion_interna

@funcion_decoradora
def funcion_normal():
    print("Soy una triste funcion normal")

funcion_normal()

# La segunda ejecución haría exactamente lo mismo si funcion_normal no estuviese decorada

############################# DECORADORES CON PARAMETROS #####################################

def dividir_inteligente(func):
    def funcion_interna(a, b):
        print(f"Voy a dividir {a} entre {b}")
        if b == 0:
            print('Ups! El divisor no puede ser 0')
    
        return func(a,b)
    return funcion_interna

@dividir_inteligente
def dividir(a, b): 
    print (a / b)




############################# ENCADENAMIENTO DE DECORADORES #####################################

# 1. Opcion con decoradores
def estrella(func): 
    def funcion_interna(msg): 
        print("*" * 15)
        print(func)
        func(msg)
        print("*" * 15)
    return funcion_interna

def porcentaje(func): 
    def funcion_interna(msg): 
        print("%" * 15)
        print(func)
        func(msg)
        print("%" * 15)
    return funcion_interna

@estrella
@porcentaje
def printer(msg):
    print(msg)

printer("hola mundo")
# 2. Opcion sin decoradores

def printer(msg):
    print(msg)

estrella(porcentaje(printer))
