############################# IMPORTAR MODULOS COMPLETOS #####################################

# 1.Importar todas las funciones de un módulo con *.
from modulo import *

crear_pizza('margarita')
sacar_dinero(1000, 100)

# 2.Importar todo el módulo.
import modulo

modulo.sacar_dinero(1000, 100)
modulo.crear_pizza('margarita')

# 3.Importar todo el módulo con un alias.
import modulo as m

m.sacar_dinero()
m.crear_pizza()

############################# IMPORTAR PARTES CONCRETAS DE UN MODULO #####################################

# 1.Importar varias funciones de un módulo.
from modulo import crear_pizza

crear_pizza('margarita')

# 2.Importar funciones con alias.
from modulo import crear_pizza as cp_funado

cp_funado('barbacoa')