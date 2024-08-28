############################# BUCLES FOR IN #####################################
#Sintaxis:
#For elemento in elementos:
#   Acciones

numeros : list = list(range(0, 11))
print(numeros)

for numero in numeros:
    numeros[numero] = numeros[numero] + 1

print(numeros)

suma : int = 0
for numero in numeros:
    suma = suma + numero

print(suma)

############################# BUCLES WHILE #####################################
#Sintaxis:
#While condicion:
#   Acciones

while suma > 0:
    #print(suma)
    suma = suma - 1
    

############################# SENTENCIAS BREAK, PASS Y CONTINUE #####################################

#Break: Detiene la ejecución del bucle.
contador: int = 0
while True: 
    contador = contador + 1 
    print(contador)
    if contador == 10:
        break

print("sigo")
#Pass: Se utiliza para dejar vacío un trozo de código que todavía no queremos especificar.
for numero in numeros:
    pass

#Continue: Pasa a la siguiente iteración del bucle.
for numero in numeros:
    if numero % 2 != 0:
        continue
    print(numero)

################### EJERCICIOS DE BUCLES #####################

################### EJERCICIO 1 #####################

# 1.Crea una lista llamada "numeros" de numeros enteros con los numeros [3,1,5,7,9,22,0].
# 2.Crea una variable llamada "numero_min" e inicializala con el primer valor de la lista.
# 3.Crea una variable llamada "numero_max" e incializala con el primer valor de la lista.
# 4.Usando un bucle "for" recorre la lista de numeros.
# 5.Utiliza un condicional "if" dentro del bucle "for" para actualizar el valor de la variable "numero_min" si el valor actual es menor.
# 6.Utiliza un condicional "if" dentro del bucle "for" para actualizar el valor de la variable "numero_max" si el valor actual es mayor.
# 7.Imprime los valores de las variables "numero_min" y "numero_max" despues de terminar el bucle.

numeros : list = [3,1,5,7,9,22,0]

numero_min : int = numeros[0]
numero_max : int = numeros[0] 

for numero in numeros:
    if numero < numero_min:
        numero_min = numero
    if numero > numero_max: 
        numero_max = numero

print(f"El numero minimo es {str(numero_min)}")
print(f"El numero maximo es {str(numero_max)}")

################### EJERCICIO 2 #####################

# 1.Crea una lista llamada "precios" con los precios de varios productos (por ejemplo: 10, 15, 20, 25, 30).
# 2.Crea una variable "descuento" con un porcentaje de descuento (por ejemplo: 0.2 para un 20% de descuento).
# 3.Usando un bucle "for" y una estructura "if-elif-else", recorre la lista "precios" y aplica el descuento correspondiente a cada precio:
# 4.Si el precio es menor a 20, no se aplica descuento.
# 5.Si el precio está entre 20 y 30, se aplica un descuento del 10%.
# 6.Si el precio es mayor a 30, se aplica el descuento establecido en la variable "descuento".
# 7.Usando la función "enumerate()" imprime el índice y el precio con descuento de cada producto.

precios : list = [10, 15, 20, 25, 30, 35]

descuento : float = 0.2

for indice, precio in enumerate(precios):
    if precio < 20: 
        print(f"El producto con indice {indice} no se le aplica descuento.")
    elif precio >= 20 and precio <= 30:
        print(f"El producto con indice {indice} se le aplica el descuento del 10% y se queda con un precio final de {precio - (precio * 0.1)} ")
    elif precio > 30:
        print(f"El producto con indice {indice} se le aplica el descuento del 20% y se queda con un precio final de {precio - (precio * descuento)} ")


################### EJERCICIO 3 #####################

# 1.Crea una lista llamada "nombres" con varios nombres (por ejemplo: Juan, Ana, Pedro, Maria, Sofia).
# 2.Crea una variable "amado_buscado" con un nombre de tu amado buscado (por ejemplo: Maria).
# 3.Crea una variable "encontrado" con valor inicial de "False".
# 4.Usando un bucle "while", una variable "indice" que empieza en 0 ,representa el numero de iteracion, y aumenta en 1 cada iteración recorre la lista "nombres" y 
#   realiza las siguientes acciones:
# 5.Si el nombres es igual a "nombre_buscado", cambia el valor de "encontrado" a "True" y mensaje "Nombre encontrado en la posicion: " y la posición del nombre.
# 6.Si "encontrado" sigue siendo "False" después de recorrer toda la lista "nombres", mensaje "Nombre no encontrado".

nombres : list = ['Juan', 'Ana', 'Pedro', 'Maria', 'Sofia']

amado_buscado : str = 'Manolo'
encontrado : bool = False
indice : int = 0

while indice <= len(nombres) - 1:
    if nombres[indice] == amado_buscado:
        encontrado = True
        print(f"Hemos encontrado a tu crush en el indice {indice}")
    indice += 1

if not encontrado:
    print(f"No hemos encontado por desgracia a tu crush.")