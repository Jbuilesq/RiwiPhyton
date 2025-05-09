#LIBRARY INVENTORY
print("="*15," LIBRERIA ","="*15)
def menu ():
    print("-"*16," MENU ","-"*16)
    print("-"*40)
    print("\nDigite una de las diguientes opciones:\n\n " \
    "1: Añadir libros.\n " \
    "2: Buscar libro por titulo.\n " \
    "3: Registrar prestamo de libro.\n " \
    "4: Devolver Libro.\n " \
    "5: Elminar libros del catalogo.\n " \
    "6: Lista de libros por genero.\n " \
    "7: Mostrar resumen de inventario\n")
    print("-"*40)

def main ():
    while True:
        menu()
        try:
            option = int(input("Ingrese una opcion: "))
            match option:
                case 1:
                    print("opcion 1")
                case _:  
                    print("Opcion invalida")
        except ValueError:
            print("Valor invalido")


main()