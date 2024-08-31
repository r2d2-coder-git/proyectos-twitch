# Sintaxis:
# class Hijo(clase_padre1, clase_padre2, clase_padre3):
#
#   Atributos clase hija
#
#   def __init__(self, atributos):
#       super().__init__(atributos_padre)
#       asignación atributos clase hija
#
#   Getters y setters de atributos de la clase hija
#
#   Metodos de la clase hija y metodos sobrecargados

    # Sobreescritura del método ganar_torneo, utilizamos la funcionalidad del padre y la extendemos para que la clase Perro pueda guardar
    # los torneos ganados.

from clases import Mascota

class Perro(Mascota):

    __color_pelo : str 
    __raza : str 
    __trofeos_ganados : dict

    def __init__(self, nombre: str , edad : int, color_pelo : str, raza : str): 
        super().__init__(nombre, edad)
        self.__color_pelo = color_pelo
        self.__raza = raza
        self.__trofeos_ganados = {'regional' : 0, 'nacional' : 0, 'internacional': 0}

    def get_color_pelo(self) -> str:
      return self.__color_pelo
    
    def set_color_pelo(self, color_pelo: str) -> None:
        self.__color_pelo = color_pelo

    def get_raza(self) -> str:
      return self.__raza
    
    def set_raza(self, raza: str) -> None:
        self.__raza = raza

    def get_trofeos_ganados(self) -> dict:
      return self.__trofeos_ganados
    
    def ganar_torneo(self, tipo_torneo : str) -> None:
       super().ganar_torneo(tipo_torneo)
       if tipo_torneo in self.__trofeos_ganados.keys():
          self.__trofeos_ganados[tipo_torneo] += 1

luisito : Perro = Perro('Luisito', 1, 'Pelirrojo', 'Lulu pomerania')


print(luisito.get_trofeos_ganados())

luisito.ganar_torneo('internacional')

print(luisito.get_trofeos_ganados())