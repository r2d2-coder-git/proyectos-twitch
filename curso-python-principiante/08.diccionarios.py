#Los diccionarios son colecciones iterables, ordenadas y mutables de elementos compuestos 
#por una clave (que identifica de modo único al elemento) y el valor que se desea almacenar. 
#No pueden aparecer elementos con claves repetidas.

#Un diccionario se utiliza cuando se quieren asociar conceptos y definiciones.

#URL: https://www2.eii.uva.es/fund_inf/python/notebooks/11_Diccionarios_conjuntos/Diccionarios_conjuntos.html

#Modulo para hacer copias profundas de diccionarios.

################### 1.CREACIÓN Y ACCESO DE DICCIONARIOS #####################

# Diccionario vacío inicializado con dict()
diccionario : dict = dict()

# Diccionario vacío inicializado con llaves
diccionario : dict = {}

#Diccionario definido comunmente

diccionario : dict = {'clave1': 1, 'clave2': 2}

# Diccionario definido con tuplas 

diccionario : dict = {('clave1', 1), ('clave2', 2)}

# Creación de un diccionario con valores constantes

diccionario : dict = dict.fromkeys(['clave1', 'clave2'], 'Valorfijo')
print(diccionario)

# Diccionario inicializado con valores
tecnologias : dict = {'Web': ['Javascript', 'Html', 'CSS'], 'Videojuegos': ['Unity', 'C#']}

################### 2.INSERCION Y ACTUALIZACION EN DICCIONARIOS #####################
tecnologias['Data Engineer'] = ['Python', 'Hadoop']
tecnologias.update({'Desarrollo Movil': ['Android', 'IOS']})
#tecnologias.update({'Web': ['Javascript', 'Html', 'CSS', 'React']})
tecnologias['Web'].append('React')
tecnologias['Web'] = []
#print(tecnologias)

################### 3.BORRADOS DE ELEMENTOS EN DICCIONARIOS #####################
valor_borrado : list = tecnologias.pop('Data Analyst', None)
ultimo_borrado : tuple = tecnologias.popitem()
#print(ultimo_borrado)
#print(tecnologias)

#tecnologias.clear()
#print(tecnologias)

################### 4.OTROS MÉTODOS #####################

tecnologias_keys : list = list(tecnologias.keys())
print(tecnologias_keys)

tecnologias_values : list = list(tecnologias.values())
print(tecnologias_values)

tecnologias_items = list(tecnologias.items())

print(tecnologias_items)

################### 5.ACCESO A ELEMENTOS EN DICCIONARIOS #####################
#[(web, []),(videojuegos, []),(data engineer, [])]

for key, value in tecnologias.items():
    print(f"La key de este elemento es {key}")
    print(f"El value de este elemento es {value}")