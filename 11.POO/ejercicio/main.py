################### EJERCICIO 1 #####################

# 7.Crea un archivo llamado "main.py" e importa la clase "Inventario" del archivo "sistema_de_inventario.py"
# 8.En el archivo "main.py" crea un objeto "inventario" de la clase "Inventario" y agrega varios objetos "Producto" al inventario utilizando el método "agregar_producto". 
# 9.Luego, realiza varias ventas y compras de productos utilizando los métodos "vender_producto" y "comprar_producto" del inventario.

from inventario import Inventario
from producto import Producto


producto1 : Producto = Producto('leche desnatada', 10, 0.8)
producto2 : Producto = Producto('piña', 5, 2.10)
producto3 : Producto = Producto('vino', 30, 5.50)
producto4 : Producto = Producto('pizza', 50, 3.20)

lista_productos = [producto1, producto2, producto3, producto4]
inventario_prueba : Inventario = Inventario() 

for producto in lista_productos:
    inventario_prueba.agregar_producto(producto)

print(inventario_prueba.get_productos())
inventario_prueba.vender_producto('leche desnatada', 5)
print(inventario_prueba.get_total_ventas())