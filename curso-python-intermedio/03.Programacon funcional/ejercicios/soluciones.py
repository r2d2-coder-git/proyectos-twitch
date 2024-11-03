################### EJERCICIOS DE PROGRAMACION FUNCIONAL #####################

################### EJERCICIO 1 #####################

# Crea una función que tome una lista de palabras y devuelva solo las palabras que tienen más de n letras. 
# Utiliza la funcion filter para lograrlo.

palabras : list = ['hola', 'mi', 'nombre', 'es', 'arturo']
def palabras_n(palabras : list, longitud : int) -> list:
    palabras_filtradas : list = list(filter(lambda palabra: len(palabra) >= longitud, palabras))
    return palabras_filtradas

palabras_filtradas : list = palabras_n(palabras, longitud=3)
print(palabras_filtradas)

################### EJERCICIO 2 #####################

# Crea una función que tome una lista de tuplas, donde cada tupla tiene un nombre y una edad, y 
# devuelva una lista de nombres de las personas mayores de edad. Utiliza funciones como filter y lambda para lograrlo.

def mayores_de_edad(personas: list[tuple[str, int]]): 
    personas_mayores_edad : list = list(filter(lambda persona: persona[1] >= 18, personas))
    nombres_personas : list = list(map(lambda persona: persona[0] , personas_mayores_edad))
    return nombres_personas

personas : list = [('Arturo', 25), ('Pepe', 19), ('Ana', 12)]

print(mayores_de_edad(personas))


################### EJERCICIO 3 #####################

# Crea dos listas, una con nombres y otra con edades, y utiliza la función zip para crear una lista de tuplas 
# con los nombres y las edades asociadas. 
# Utiliza la función all para verificar si todas las edades son 
# mayores de 18 y la función any para verificar si hay alguna edad menor a 18.

nombres : list = ['arturo', 'alejandro', 'pepe']
edades : list = [10, 15, 17]

personas : list  = list(zip(nombres, edades))
personas_map :list = list(map(lambda persona: True if persona[1] >= 18 else False , personas))
print(personas_map)
todos_mayores : bool = all(personas_map)
algun_mayor : bool = any(personas_map)

print(algun_mayor)

