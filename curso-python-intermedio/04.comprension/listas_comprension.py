# Las listas de comprensión y los diccionarios de comprensión son características poderosas en Python que te permiten 
# crear listas y diccionarios de manera más concisa y legible.

# Con las listas de comprensión, puedes aplicar una expresión a cada elemento de una secuencia y generar una nueva 
# lista basada en los resultados.

# Los diccionarios de comprensión funcionan de manera similar, pero permiten crear diccionarios directamente.

# Ventajas:

# 1. Código más conciso y legible
# 2. Mejor rendimiento (Python lo optimiza super bien)
# 3. Menos propenso a errores


############################# LISTAS DE COMPRENSIÓN #####################################

# Crear una lista de números al cuadrado usando un bucle for
numeros : int = [1,2,3,4,5]
cuadrados : list = []
for numero in numeros: 
    cuadrados.append(numero**2)

print(cuadrados)
# Crear una lista de números al cuadrado usando una lista de comprensión
cuadrados_comp : list = [numero**2 for numero in numeros]
print(cuadrados_comp)

# Filtrar números pares y elevarlos al cuadrado
pares_cuadrados : list = [numero**2 for numero in numeros if numero % 2 == 0]

############################# DICCIONARIOS DE COMPRENSIÓN #####################################

# Crear un diccionario con números y sus cuadrados usando un bucle for
cuadrados_dict = {}
for numero in numeros: 
    cuadrados_dict[numero] = numero**2

print(cuadrados_dict)
# Crear un diccionario con números y sus cuadrados usando un diccionario de comprensión
cuadrados_dict_comp : dict = {numero: numero**2 for numero in numeros}
print(cuadrados_dict_comp)

# Filtrar números pares y crear un diccionario con su valor original y su cuadrado
cuadrados_dict_comp : dict = {numero: numero**2 for numero in numeros if numero % 2 == 0}
print(cuadrados_dict_comp)

############################# LISTAS DE COMPRENSIÓN CON ANIDADAS #####################################

# Crear una lista de pares (x, y) donde x e y sean elementos de dos listas diferentes
lista_1 : list = [1,2,3]
lista_2 : list = [4,5,6]

lista_3 : list  = []
for x in lista_1:
    for y in lista_2:
        if x+y > 5: 
            lista_3.append((x,y))


pares : list = [(x,y) for x in lista_1 for y in lista_2]
print(pares)

# Filtrar y crear una lista de pares solo si la suma de x e y es mayor que 5

numeros_filtrados : list = [(x,y) for x in lista_1 for y in lista_2 if x + y > 5]

print(numeros_filtrados)

############################# DICCIONARIOS DE COMPRENSIÓN CON ANIDADAS #####################################

# Crear un diccionario con claves de lista_1 y valores como listas de elementos de lista_2
dict_anidado : dict = {x: [y for y in lista_2] for x in lista_1}
print(dict_anidado)

# Crear un diccionario con claves de lista_1 y valores como listas filtradas de elementos de lista_2
dict_anidado : dict = {x: [y for y in lista_2 if y > 4] for x in lista_1}
print(dict_anidado)


############################# CONVERSIÓN DE LISTA A DICCIONARIO Y VICEVERSA #####################################
lista_de_tuplas : list = [('a', 1), ('b', 2), ('c', 3)]

# Convertir una lista de tuplas en un diccionario
dict_from_list : dict = {key : value for key, value in lista_de_tuplas}

# Convertir un diccionario en una lista de tuplas
lista_de_tuplas_2 : list = [(key, value) for key, value in dict_from_list.items()]
print(lista_de_tuplas_2)
############################# MEDICIÓN DE RENDIMIENTO #####################################

import time 

diccionario_grande : dict = {numero : numero for numero in range(10000000)}

# Usando lista de comprensión
start = time.time()
values : list = [key for key in diccionario_grande.values()]
print(f"Tiempo con lista de comprension: {time.time() - start}")

#Usando un map de programacion funcional
start = time.time()
values : list = list(diccionario_grande.values())
print(f"Tiempo con map: {time.time() - start}")


# Usando bucle for

#start = time.time()
#cuadrados = []
#for n in range(10000000): 
#    cuadrados.append(n**2)
#print(f"Tiempo con bucles: {time.time() - start}")

