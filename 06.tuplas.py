# Una diferencia importante entre las tuplas y las listas es que las tuplas son más rápidas que las listas en términos de eficiencia y rendimiento. 
# Esto se debe a que las tuplas son inmutables, lo que significa que el interprete de Python puede optimizar el uso de la memoria y el acceso a los elementos de la 
# tupla de manera más eficiente que en el caso de las listas.

# En general, se recomienda utilizar tuplas en casos donde se necesite una estructura de datos que no pueda ser 
# modificada, como por ejemplo cuando se quiera representar un conjunto de valores constantes. Por otro lado, se recomienda utilizar listas en casos donde se 
# necesite una estructura de datos que pueda ser modificada, como por ejemplo cuando se quiera almacenar una secuencia de elementos que puedan ser cambiados 
# en el transcurso del programa.

#Enlace de la web: https://stackoverflow.com/questions/14135542/how-is-tuple-implemented-in-cpython

#Las tuplas son ordenadas.
#Las tuplas son inmutables
#Las tuplas permiten valores duplicados.

################### 1.CREACIÓN DE TUPLAS #####################
tupla_vacia : tuple = ()
tupla_vacia : tuple = tuple()

print(tupla_vacia)

################### 2.INSERTAR Y ACTUALIZAR #####################
#Las tuplas no cuentan con métodos de inserción y actualización puesto que son inmutables, una vez creadas no se pueden cambiar.
tupla_uno : tuple = ('Arturo', 'Lorenzo', 'Hernandez')
tupla_dos : tuple = ('R2D2', 'Coder', 'Coder')
print(tupla_uno)
################### 3.BORRADOS #####################
#del tupla_uno

################### 4.OPERACIONES DE TUPLAS #####################
tupla_tres : tuple = tupla_uno + tupla_dos
index_arturo : int = tupla_uno.index('Arturo')
count_coder : int = tupla_dos.count('Coder')

print(index_arturo)
print(count_coder)

################### 5.OTROS METODOS #####################

tupla_num : tuple = (1,2,3)
print(len(tupla_num))
print(min(tupla_num))
print(max(tupla_num))
print(sum(tupla_num))

################### 6.ACCESO A LOS TUPLAS #####################
print("ACCESO TUPLAS")
# Acceso de forma indexada
print(tupla_num[0])
# Acceso con intervalos de elementos
print(tupla_num[0:2])

# Acceso con bucle for
for numero in tupla_num:
    print(numero)