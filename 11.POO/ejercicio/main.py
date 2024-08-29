################### EJERCICIO 1 #####################

# 1.Crea un archivo llamado "sistema_de_inventario.py" y define una clase llamada "Producto" con atributos como "nombre", "cantidad" y "precio". 
# 2.También define un método llamado "vender" que reciba una cantidad como argumento, reste esa cantidad al atributo "cantidad" del producto
#   y retorne True or False si la venta es posible . 
# 3.También define un método llamado "comprar" que reciba una cantidad como argumento, sume esa cantidad al atributo "cantidad" del producto y no retorne nada.
# 4.Crea otra clase llamada "Inventario" con atributos como "productos" que es una lista vacía y "total_ventas" que es un número. 
# 5.También define un método "agregar_producto" que reciba un objeto "Producto" como argumento y lo agregue a la lista de productos del inventario. 
#     Otro método es "vender_producto" que reciba el nombre del producto y una cantidad, busque el producto correspondiente en la lista de productos y llame al método "vender" en ese producto. 
#     Ademas, suma el precio total de la venta al atributo "total_ventas" del inventario.
# 6.Crea otro método en la clase Inventario llamado "comprar_producto" que reciba el nombre del producto y una cantidad, busque el producto correspondiente en la lista de productos y 
#     llame al método "comprar" en ese producto.
# 7.Crea un archivo llamado "main.py" e importa la clase "Inventario" del archivo "sistema_de_inventario.py"
# 8.En el archivo "main.py" crea un objeto "inventario" de la clase "Inventario" y agrega varios objetos "Producto" al inventario utilizando el método "agregar_producto". 
# 9.Luego, realiza varias ventas y compras de productos utilizando los métodos "vender_producto" y "comprar_producto" del inventario.