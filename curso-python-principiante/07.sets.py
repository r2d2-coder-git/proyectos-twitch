#La estructura de datos utilizada en SET es Hashing, una técnica popular para realizar inserción, eliminación y recorrido en O(1) en promedio. 
#Las operaciones en Hash Table son algo similares a las de Linked List. Los sets en python son una lista desordenada con elementos duplicados eliminados.
#Un set es un mapa hash con linked list desordenadas. Por eso es mejor utilizar set que list cuando el orden de inserción y eliminación nos den igual.

#Enlace en la web: https://www.codesansar.com/python-programming/how-sets-are-internally-stored-python.htm

#Los sets establecidos no están ordenados, es decir, cuando se añade un elemento o se borra no se sabe en que posición del set va a caer.
#Los elementos de un set no se pueden modificar, es decir, no puedes sobreescribir una posición de un set, pero si puedes hacer inserciones y borrados en el set. 
#Los sets no permiten valores duplicados.

"""


[0, 1, 2, 3, 4]

[0,             1]
[0,2,4]        [1,3]



"""

################### 1.CREACIÓN DE SETS #####################

# 1. set vacío
nuevo_set : set = set()

# 2. Inicializar un set con elementos
nuevo_set : set = {'uno', 'dos'}

################### 2.INSERTAR Y ACTUALIZAR #####################
nuevo_set.add('cuatro')
#print(nuevo_set)
nuevo_set.update({'tres', 'dos'})
#print(nuevo_set)
copia_set : set = nuevo_set.copy()

#print(nuevo_set)
#print(copia_set)

################### 3.BORRADOS #####################

nuevo_set.discard('cincuenta')
#print(nuevo_set)
nuevo_set.remove('tres')
#print(nuevo_set)
nuevo_set.clear()
#print(nuevo_set)

################### 4.OPERACIONES DE SETS #####################

# ***Los siguientes métodos devuelven un conjunto nuevo, no modifican el conjunto. ***
set_uno : set = {1,2,3,4}
set_dos : set = {4,5,6,7}

set_diferencia : set = set_uno.difference(set_dos)
set_interseccion : set = set_uno.intersection(set_dos)
set_union : set = set_uno.union(set_dos)
set_diferencia_simetrica : set = set_uno.symmetric_difference(set_dos)
#print(set_diferencia_simetrica)

#print(dir(set_uno))



# ***Los siguientes métodos modifican el conjunto sobre el que se aplica el método. ***
#set_uno.difference_update(set_dos)

#print(set_uno)


################### 5.OTROS METODOS #####################

es_subcojunto : bool = set_uno.issubset(set_dos)
es_superconjunto : bool = set_uno.issuperset(set_dos)
no_tiene_interseccion : bool = set_uno.isdisjoint(set_dos)
print(no_tiene_interseccion)


################### 6.ACCESO A LOS SETS #####################

#No hay una forma de acceder de forma indexada
for elemento in set_uno:
    print(elemento)