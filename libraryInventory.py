#LIBRARY INVENTORY
print("="*15," LIBRERIA ","="*15)

bookInventory = []
literaryGenre = ["Fiction", "Non-Fiction", "Science", "Biography", "Children"]

def selectGenre ():
    print("\nSeleccione el genero del libro: \n")
    print(f"1: {literaryGenre[0]}.\n"
          f"2: {literaryGenre[1]}.\n"
          f"3: {literaryGenre[2]}.\n"
          f"4: {literaryGenre[3]}.\n"
          f"5: {literaryGenre[4]}.\n")
    while True:
        try:
            option = int(input("Ingrese una opción: "))
            match option:
                case 1:
                    print(f"El genero del libro es {literaryGenre[0]}.")
                    return literaryGenre[0]
                case 2:
                    print(f"El genero del libro es {literaryGenre[1]}.")
                    return literaryGenre[1]
                case 3:
                    print(f"El genero del libro es {literaryGenre[2]}.")
                    return literaryGenre[2]
                case 4:
                    print(f"El genero del libro es {literaryGenre[3]}.")
                    return literaryGenre[3]
                case 5:
                    print(f"El genero del libro es {literaryGenre[4]}.")
                    return literaryGenre[4]
                case 6:
                    print("Ingresaste un valor incorrecto.")  
                
        except ValueError:
            print("Ingresaste un valor incorrecto.")            
            

def addBook ():
    nameBook = input("Ingrese el titulo del libro: ")
    authorBook = input("ingrese el autor del libro: ")
    numberOfCopie = int(input("Ingrese el numero de copias: "))
    bookGenre = selectGenre()
    bookLoan = int(input("Ingrese el numero de copias prestadas: "))
    bookInventory.append({"bookTitle":nameBook,"authorBook":authorBook,"numberOfCopies":numberOfCopie,"bookGenre":bookGenre,"bookLoan":bookLoan})

def book():
    searchBook = input("Ingrese el libro que desea buscar: ")
    for book in bookInventory:
        if book["bookTitle"] == searchBook:
            print("El libro se ha encontrado")
            return
    print("El libro no fue encontrado: ")

def booksLoan():
    searchBook = input("Ingrese el libro que desea prestar: ")
    for book in bookInventory:
        if book["bookTitle"] == searchBook:
            print(book["bookTitle"],book["numberOfCopies"],book["bookLoan"])
            print(type(book["bookTitle"],book["numberOfCopies"],book["bookloan"]))
            if book["bookloan"] != 0:#book["numberOfCopies"]:
                print("El libro tiene copias disponibles")
                book["bookLoan"] += 1
                print(f"numero de copias disponibles {book["numberOfCopies"]-book["bookLoan"]}")
                return
            else:
                print("No hay copias disponibles para prestamo: ")
    print("El libro no fue encontrado: ")


def menu ():
    print("\n","-"*16," MENU ","-"*16)
    print("-"*40)
    print("\nDigite una de las diguientes opciones:\n\n " \
    "1: Añadir libros.\n " \
    "2: Buscar libro por titulo.\n " \
    "3: Registrar prestamo de libro.\n " \
    "4: Devolver Libro.\n " \
    "5: Eliminar libros del catalogo.\n " \
    "6: Lista de libros por genero.\n " \
    "7: Mostrar resumen de inventario\n " \
    "8: Salir.\n")
    print("-"*40)

def main ():
    while True:
        menu()
        try:
            option = int(input("Ingrese una opcion: "))
            match option:
                case 1:
                    print("\n","-"*10," AÑADIR LIBRO. ","-"*10,"\n") #Permitir al usuario agregar libros con atributos como título, autor, cantidad de copias disponibles y género literario.
                    addBook()
                case 2:  
                    print("\n","-"*10," BUSCAR LIBROS POR TITULO ","-"*10,"\n") #Permitir consultar los detalles de un libro por su título (autor, copias disponibles, género).
                    book()
                    print(literaryGenre)
                    print(bookInventory)
                case 3:
                    booksLoan()
                    print("\n","-"*10," REGISTRAR PRESTAMO DE LIBRO ","-"*10,"\n") #Disminuir en 1 la cantidad de copias disponibles al registrar un préstamo. Validar que haya copias disponibles antes de prestarlo.
                case 4:
                    print("\n","-"*10," DEVOLVER LIBRO ","-"*10,"\n")#Aumentar en 1 la cantidad de copias disponibles al registrar una devolución.
                case 5:
                    print("\n","-"*10," ELIMINAR LIBROS DEL CATALOGO ","-"*10,"\n") # Permitir eliminar libros si no tienen copias prestadas (cantidad = total original).
                case 6:
                    print("\n","-"*10," LISTA DE LIBROS POR GENERO  ","-"*10,"\n") #Mostrar todos los libros disponibles de un género específico.
                case 7:
                    print("\n","-"*10," MOSTRAR INVENTARIO ","-"*10,"\n") #Indicar cuántos libros hay en total y cuántas copias en total están disponibles en la biblioteca.
                case 8:
                    print("\n","-"*10," SALIR ","-"*10,"\n")
                    break
                case _:
                    print("\n","-"*10," Ingesaste una opción no valida. ","-"*10,"\n")
        except ValueError:
            print("Valor invalido")


main()