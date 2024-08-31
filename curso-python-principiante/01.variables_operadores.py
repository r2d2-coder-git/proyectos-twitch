# Soy un comentario de una linea 

"""
Soy el comentario multilinea
"""

# TIPOS DE DATOS EN PYTHON 

#Numericos

contador : int = 0
numero_pi : float = 3.14
imaginario : complex = -5j

#Booleanos

es_verdad : bool = True
es_mentira : bool = False

#String
mi_nombre : str = 'arturo lorenzo'

# OPERADORES

# OPERADORES ARITMETICOS 

suma : int = 1 + 1 
resta : int = 1 - 1
multiplicacion : int = 10 * 10
division_con_decimales : float = 18 / 5
print(division_con_decimales)
division_sin_decimales : int = 18 // 5
print(division_sin_decimales)
modulo : int = 11 % 10 

# OPERADORES RELACIONALES 

mayor_que : bool = 2 > 1
print(mayor_que)
menor_que : bool = 2 < 1
print(menor_que)
igual_que : bool = 1 == 1
mayor_o_igual_que : bool = 2 >= 2
distinto_que : bool = 2 != 1

# OPERADORES LOGICOS 

and_operation : bool = True and True 
or_operation : bool = False or False
not_operation : bool = not True 
print(not_operation)

# OPERADORES DE PERTENENCIA 

in_operation : bool = "hola" in "hola mundo"
not_operation : bool = "arturo" not in "hola mundo"

# OPERADORES DE IDENTIDAD 
x = 1
y = x
nulo = None

is_operation = x is y

check_nulo = nulo is not None
print(is_operation)
print(check_nulo)
