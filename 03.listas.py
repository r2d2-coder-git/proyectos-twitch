#Las listas hacen uso de arrays de longitud variable internamente, los arrays de longitud variable son una variante de los arrays 
#cuyo tamaño no se especifica inicialmente, o cuya longitud o tamaño se establece durante el tiempo de ejecución, 
#también puede llamarlos arreglos automáticos, se van redimensionando según las necesidades del programa, se dicen arrays automáticos porque cada vez que se hace un append 
#se guardan en memoria más espacio del que se necesita para prevenir redimensionar muchas veces.

#Enlace de la web: https://towardsdatascience.com/how-lists-in-python-are-optimised-internally-for-better-performance-847c8123b7fa

#Las listas en Python son ordenadas, quiere decir que cada vez que se añade un elemento tiene un orden definido, se va al final de la lista. Y cada vez que se borra un elemento
#se corren los elementos de la derecha una posición a la izquierda. [0,1,2,3,4] -> Quitamos el 2 -> [0,1,3,4]
#Las lista son cambiantes, es decir, se pueden actualizar los valores de sus elementos. 
#Las listas permiten valores duplicados.

################### 1.CREACIÓN DE LISTAS #####################

# 1. Lista vacía
lista_vacia : list = []
lista_vacia : list = list()
print(lista_vacia)

# 2. Lista con elementos
motocicletas : list = ["honda", "yamaha", "suzuki", "honda"]

#print(motocicletas)
################### 2.INSERCIONES Y ACTUALIZACIONES #####################
motocicletas.append('ducati')
#print(motocicletas)
motocicletas.insert(2, 'daelim')
#print(motocicletas)

motocicletas[1] = 'bmw'
#print(motocicletas)

################### 3.BORRADOS #####################
motocicletas : list = ["honda", "yamaha", "suzuki", "honda"]
#print(motocicletas)
elemento_cero : str = motocicletas.pop(0)
ultimo_elemento : str = motocicletas.pop()
motocicletas.remove('yamaha')
#print(motocicletas)
motocicletas.clear()

#Borrar todas las apariciones de un elemento en una lista
#while 'honda' in motocicletas:
#    motocicletas.remove('honda')

#print(motocicletas)

################# 4.SORT ######################
vocales : list = ['e','i','u','o','a']
vocales.sort()
vocales.sort(reverse=True)
#print(vocales)

def ordenar_por_longitud(elemento : str) -> int: 
    return len(elemento)

coches : list = ['Ford', 'Toyota', 'BMW']
coches.sort(key=ordenar_por_longitud, reverse=True)
#print(coches)

################# 5.ACCESO A LAS LISTAS ######################

# La forma de acceder a los elementos de una lista es con el operador [inicio:fin]. Indicando el inicio de elementos que quieres de la lista
# y fin indica el elemento - 1 que va recoger de la lista. Los indices empiezan en 0.
numeros : list = [10, 20, 30, 40, 50]

primer_elemento: int = numeros[0]
#print(primer_elemento)
dos_primeros_elementos: list = numeros[0:2]
#print(dos_primeros_elementos)
ultimo_elemento = numeros[-1]
dos_ultimos_elementos = numeros[-2:]
#print(dos_ultimos_elementos)

# También podemos indicar cada X número de elementos coger un elemento. Con un tercer separador lista[inicio:fin:numero_saltos]. Si numero_saltos
# es positivo entonces empezamos desde el principio de la lista hasta el final, si numero_saltos es negativo empezamos desde el final hasta el 
# principio.

todos_elementos : list = numeros[::1]
indices_impares : list = numeros[::2]
indices_pares : list = numeros[1::2]
lista_reversa : list = numeros[::-1]
print(lista_reversa)

################# 6.OTROS MÉTODOS ######################




# 1.BIS. Rangos númericos con la función range(x,y-1) El tipico for (i; i < x; i++) eso en python no existe.


# 2.BIS. Funciones Built-in de python que se pueden aplicar sobre las listas

# Minimo de una lista
# Maximo de una lista
# Suma los elementos de la lista
# Longitud de la lista
# Si queremos ver una lista ordenada pero no ordenarla realmente. 