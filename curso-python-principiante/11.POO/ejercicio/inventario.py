# 4.Crea otra clase llamada "Inventario" con atributos como "productos" que es una lista vacía y "total_ventas" que es un número. 
# 5.También define un método "agregar_producto" que reciba un objeto "Producto" como argumento y lo agregue a la lista de productos del inventario. 
#     Otro método es "vender_producto" que reciba el nombre del producto y una cantidad, busque el producto correspondiente en la lista de productos y llame al método "vender" en ese producto. 
#     Ademas, suma el precio total de la venta al atributo "total_ventas" del inventario.
# 6.Crea otro método en la clase Inventario llamado "comprar_producto" que reciba el nombre del producto y una cantidad, busque el producto correspondiente en la lista de productos y 
#     llame al método "comprar" en ese producto.

from producto import Producto

class Inventario():

    __productos : list 
    __total_ventas : int 

    def __init__(self) -> None:
        self.__productos  = list()
        self.__total_ventas = 0
    
    def get_productos(self) -> list: 
        nombres_producto : list = []
        for producto in self.__productos:
            nombres_producto.append(producto.get_nombre())
        return nombres_producto
    
    def get_total_ventas(self) -> int:
        return self.__total_ventas
    
    def agregar_producto(self, producto: Producto) -> None:
        if producto in self.__productos:
            print(f"Este producto ya está en el inventario, añade uno diferente") 
            return None
        
        self.__productos.append(producto)

        print(f"Has añadido el producto {producto.get_nombre()} a tu inventario.")
        return None
    
    def vender_producto(self, nombre_producto : str, cantidad : int) -> None:
        for producto_inventario in self.__productos:
            if producto_inventario.get_nombre() == nombre_producto:
                venta_realizada : bool = producto_inventario.vender(cantidad)
                if venta_realizada:
                    self.__total_ventas += producto_inventario.get_precio() * cantidad
            
        print(f"Ahora tu cashflow es de {self.__total_ventas}")
        return None

    
    def comprar_producto(self, nombre_producto : str, cantidad : int) -> None:
        for producto_inventario in self.__productos:
            if producto_inventario.nombre == nombre_producto: 
                producto_inventario.comprar(cantidad)
        
        return None
