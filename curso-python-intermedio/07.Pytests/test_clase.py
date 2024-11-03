############################## ¿COMO SE TESTEA UNA CLASE? #####################################


############################## 1. MANERA INEFICIENTE DE HACERLO #####################################




# Este test es ineficiente ya que tenemos que crear un objeto Encuesta por cada llamada al método 
# test_guardar_una_respuesta.


############################## 2. MANERA EFICIENTE DE HACERLO #####################################

# Python ejecuta el metodo setUp antes de ejecutar cada método que empiece por test_ dentro de una clase que hereda 
# de unittest.TestCase.
# Por ello si sobreescribimos este método para inicilizar los objetos que vamos a usar en los tests nos ahorraremos 
# mucha memoria evitando crear un objeto por test.



# Esta llamada a main ejecuta los 3 tests aunque vengan de clases distintas porque las dos heredan de unittest.TestCase

