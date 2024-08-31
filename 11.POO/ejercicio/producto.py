# 1.Crea un archivo llamado "sistema_de_inventario.py" y define una clase llamada "Producto" con atributos como "nombre", "cantidad" y "precio". 
# 2.También define un método llamado "vender" que reciba una cantidad como argumento, reste esa cantidad al atributo "cantidad" del producto
#   y retorne True or False si la venta es posible . 
# 3.También define un método llamado "comprar" que reciba una cantidad como argumento, sume esa cantidad al atributo "cantidad" del producto y no retorne nada.


class Producto():

    __nombre : str
    __cantidad : int 
    __precio : float

    def __init__(self, nombre : str, cantidad: int, precio : float) -> None:
        self.__nombre = nombre
        self.__cantidad = cantidad 
        self.__precio = precio

    def get_nombre(self) -> str:
        return self.__nombre
    
    def set_nombre(self, nombre : str):
        self.__nombre = nombre
    
    def get_cantidad(self) -> str:
        return self.__cantidad
    
    def set_cantidad(self, cantidad : str):
        self.__cantidad = cantidad
    
    def get_precio(self) -> int:
        return self.__precio
    
    def set_precio(self, precio : int):
        self.__precio = precio

    def vender(self, cantidad : int) -> bool:
        if self.__cantidad < cantidad:
            print(f'No hay tantos ejemplares de este producto, solo nos quedan {self.__cantidad}')
            return False
        
        self.__cantidad -= cantidad
        print(f'Has vendido {cantidad} de unidades de {self.__nombre}, ahora te quedan {self.__cantidad}')
        return True
    
    def comprar(self, cantidad : int) -> None: 
        self.__cantidad += cantidad 
        return None
        