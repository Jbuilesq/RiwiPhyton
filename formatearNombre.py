#Formatear un nombre completo ingresado por el usuario, asegurando que cada parte del nombre esté en minúsculas y la primera letra en mayúscula.

#función para formatear el nombre
def formatearNombres():
    #Solicitar al usuario que ingrese su nombre, segundo nombre y apellido
    nombre = input("Ingrese su nombre: ")
    segundo_nombre = input("Ingrese su segundo nombre: ")
    apellido = input("Ingrese su apellido: ")

   
    # Con lower() convertimos a minúsculas, capitalize() convierte la primera letra a mayúscula y strip() elimina espacios en blanco al inicio y al final
    nombre = nombre.lower().capitalize().strip()
    segundo_nombre = segundo_nombre.lower().capitalize().strip()
    apellido = apellido.lower().capitalize().strip()

    return f"{nombre} {segundo_nombre} {apellido}"

nombreCompleto = formatearNombres()
print(f"Nombre formateado: {nombreCompleto}")