
import re

# 1. Extraer todas las direcciones de correo electrónico de un texto.
texto = "Contacta con nosotros: info@empresa.com, soporte@ayuda.org"
patron_email = r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b"
correos = re.findall(patron_email, texto)
print("Correos encontrados:", correos)

