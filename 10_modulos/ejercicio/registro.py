from validaciones import validar_email

def registrar_usuario(nombre: str, email: str) -> None:
    if validar_email(email):
        print(f"Tu usuario con nombre {nombre} ha sido registrado con éxito con el correo {email}.")
        return
    
    print(f"Tu email no es valido no puede empezar con @ y tiene que terminar con @gmail.com")
    return 
