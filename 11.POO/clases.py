
# Sintaxis:

# class NombreClase():
#   Atributos
#   def __init__(self):
#       Inicializar atributos (constructor)
#   Setters and getters
#   Metodos de clase
#

# Implementación de la clase mascota para un videojuego de animales.

class Mascota():
     
    ############################# ATRIBUTOS DE LA CLASE #####################################
    __nombre : str 
    __puntos_salud : int 
    __nivel : int
    __edad : int 

    ############################# CONSTRUCTOR DE LA CLASE #####################################
    def __init__(self, nombre : str, edad : int ):
        self.__nombre = nombre
        self.__edad = edad
        self.__nivel = 1
        self.__puntos_salud = 10

    ############################# METODOS GETTERS AND SETTERS #####################################

    # Los metodos getters y setters sirven para ofrecer la funcionalidad de obtener el valor o cambiar el valor de los atributos que queremos darle 
    # la posibilidad al programador que utilice la clase.

    # Sintaxis getters: (Los atributos deben ser privados o protegidos, sino no tendría sentido hacer un get o set ya que podemos modificar y
    # consultar los atributos directamente, es más daría un bucle infinito.)
    
    # def get_atributo(self) -> tipo_atributo:
    #   return self.__nombre_atributo

    # Sintaxis setters:
    # def set_atributo(self, value) -> None:
    #   self.__nombre_atributo = value

    def get_nombre(self) -> str:
      return self.__nombre
    
    def set_nombre(self, nombre: str) -> None:
        self.__nombre = nombre

    def get_edad(self) -> int:
      return self.__edad
    
    def set_edad(self, edad: int) -> None:
        self.__edad = edad

    def get_puntos_salud(self) -> int:
      return self.__puntos_salud
    
    def set_puntos_salud(self, puntos_salud: int) -> None:
        self.__puntos_salud = puntos_salud

    def get_nivel(self) -> int:
      return self.__nivel
    
    def set_nivel(self, nivel: int) -> None:
        self.__nivel = nivel

  ############################# METODOS DE CLASE #####################################

  # Método que sirve para aumentar la salud a tu mascota.
    def alimentar_mascota(self, comida : str) -> None:
      if comida == 'comida_normal':
        self.__puntos_salud += 10
      elif comida == 'comida_buena': 
         self.__puntos_salud += 20
      elif comida == 'comida_genial':
         self.__puntos_salud += 30
      
      print(f'Mmm... que rico! Ahora me siento más fuerte y tengo {self.__puntos_salud} puntos de salud.')
       

  # Método que sirve para aumentar de nivel a tu mascota en función del torneo que haya ganado.

    def ganar_torneo(self, tipo_torneo: str) -> None:
      if tipo_torneo == 'regional':
        self.__nivel += 1
      elif tipo_torneo == 'nacional':
        self.__nivel +=2
      elif tipo_torneo == 'internacional':
         self.__nivel += 3
      
      print(f'Enhorabuena {self.__nombre} has ganado un torneo {tipo_torneo}! Has subido de nivel al nivel {self.__nivel}')

#nemo_mascota : Mascota = Mascota(nombre='Nemo', edad='3')
#
#print(nemo_mascota.get_puntos_salud())
#
#nemo_mascota.alimentar_mascota('comida_normal')
#
#nemo_mascota.ganar_torneo('regional')