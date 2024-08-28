############################# SINTAXIS #####################################

#CONDICION SIMPLE

#if condition1:
#   accion1
#elif condition2:
#   accion2
#else:
#   accion3

#CONDICION ANIDADA

#if condition1:
#   if condition2:
#       action1
#   elif condition3:
#       action2
#   else: 
#       action3
#elif condition4:
#   action4

############################# CONDICIONAL BOOLEANO #####################################
valor_booleano: bool = False

if valor_booleano: 
    print("El valor booleano es true")


############################# CONDICIONAL BOOLEANO CON ELSE ##################################### 
if valor_booleano: 
    print("El valor booleano es true")
else: 
    print("El valor es falso")

############################# CONDICIONAL NUMÉRICO #####################################

edad : int = 18

if edad >= 18 and edad <80: 
    print("Enhorabuena puedes conducir un coche!")
else: 
    print("O todavia eres muy pequeño o ya no estas pa conducir")

############################# CONDICIONAL NUMÉRICON CON ELIF #####################################

#dinero : int = int(input("Oye tu! Cuanto dinero tienes?"))

#if dinero > 1000:
#    print("Eres rico!")
#elif dinero > 500: 
#    print("Tienes dinerillo")
#elif dinero > 100:
#    print("hay que seguir estudiando programacion")
#else: 
#    print("Eres pobre...")

############################# CONDICIONALES CON STRINGS #####################################
#nombre : str = input("¿Cómo te llamas? ")
#
#if nombre == 'r2d2.coder': 
#    print("eres el autentico")
#else: 
#    print("eres un farsante")


nombre : str = None

if nombre:
    print("El string existe")
else:
    print("El string es vacio")

############################# CONDICIONALES CON LISTAS #####################################
nombres : list = []

if 'arturo' in nombres and 'naxete' in nombres:
    print("Tenemos a arturo y naxete en la lista")
else: 
    print("no tenemos a arturo o a naxete en la lista")


if nombres: 
    print("la lista no esta vacia")
else: 
    print("la lista esta vacia")

############################# CONDICIONALES INLINE #####################################

# Es mucho más legible que poner if elif else asignando tres veces un valor a una variable.
# Sintaxis: Action1 if condition1 else Action2 if condition2 else Action3

dinero : int = 5

estatus_economico : str = 'Clase alta' if dinero > 1000 else 'Clase Media' if dinero > 500 else 'Clase Baja'
