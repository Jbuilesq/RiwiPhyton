def formatearNombres():
    nombre = input("Ingrese su nombre: ")
    segundo_nombre = input("Ingrese su segundo nombre: ")
    apellido = input("Ingrese su apellido: ")

    nombre = nombre.lower().capitalize().strip()
    segundo_nombre = segundo_nombre.lower().capitalize().strip()
    apellido = apellido.lower().capitalize().strip()

    return f"{nombre} {segundo_nombre} {apellido}"

resultado = formatearNombres()
print(f"Nombre formateado: {resultado}")