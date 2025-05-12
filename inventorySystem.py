#INVENTORY SYSTEM

print("="*15," SISTEMA DE INVETARIO ","="*15)

#Is declared this goblal variable to use in all funtion.
productInventoryList = []

#This function is used to display the menu options.
def menu ():
    print("\n","-"*16," MENU ","-"*16)
    print("-"*40)
    print("\nDigite una de las diguientes opciones:\n\n " \
    "1: Añadir producto.\n " \
    "2: Buscar producto.\n " \
    "3: Actualizar precio de producto.\n " \
    "4: Eliminar libros del catalogo.\n " \
    "5: Valor total del inventario.\n " \
    "6: Salir.\n")
    print("-"*40)

#This funtion is used to validate that the input quantity and value numbers are positive.
def valueValidation (cantValue):
    while True:
        try:
            value = float(input(f"Ingrese {cantValue}"))
            while value < 0:
                value = float(input(f"Error: Ingrese {cantValue}"))
            return value
        except ValueError:
            print (f"Error: {cantValue} debe ser en numeros.")

#This funtion is used to validate the product list and create a new product. if a product is entered by the first time you have to enter five product.       
def addProduct():
    while True:
        print("\n""-"*10,"Añadir nuevo producto","-"*10,"\n")
        nameProduct = input("Ingrese el nombre del producto agregar: ").strip().lower().capitalize()
        while nameProduct == "":
            nameProduct = input("Error: Ingrese el nombre del producto agregar: ").strip().lower().capitalize()
        for product in productInventoryList:
            if product["nameProduct"] == nameProduct:
                print(f"¡¡¡El producto {product['nameProduct']} ya existe y no se puede crear de nuevo!!! ")
                return
        priceProduct = valueValidation("el precio del producto en UNDS: $") 
        productQuantity = int(valueValidation("la cantidad de producto: "))
        productInventoryList.append({"nameProduct":nameProduct,"priceProduct":priceProduct,"productQuantity":productQuantity})
        if len(productInventoryList) >= 5:
            option = input("\nIngrese 1: Para ingresar mas productos O Ingrese: Cualquier tecla para volver al menu: ")
            if option == "1":
                print("\n")
                continue
            else:
                break

#This lambda is used to multiply the price of the products by their quantity of units.
multiplyProduct = lambda x,y : x*y

#this funtion is used to search, modify or delect products.   
def   searchModifyOrDeleteProduct (option,txtOption):
    if len(productInventoryList) ==  0:#Here is validated if the list (productInvetoryList) is empty. if this is true the user have to enter products.
        print("Primero debe agregar productos para realizar cualquier otra acción: \n")
        addProduct()
        return
    nameProduct = input(f"Ingrese el nombre del producto que desea {txtOption}: ").strip().lower().capitalize()
    while nameProduct == "":
        nameProduct = input(f"Error: Ingrese el nombre del producto que desea {txtOption}: ").strip().lower().capitalize()
    for product in productInventoryList: #Here is iterate the list
        if product["nameProduct"] == nameProduct: #Here its validated if the product already exists.
            print(f"\nEl producto {product['nameProduct']} se ha encontrado! \n")
            if option == 2: #Here its executed the second option(show datails about the product).
                print(f"Producto: {product['nameProduct']} | Precio: ${product['priceProduct']:.2f} | Cantidad: {product['productQuantity']} | Precio total: {multiplyProduct(product['priceProduct'],product['productQuantity']):.2f}")
                return
            elif option == 3:#Here its executed the third option (price changed)
                print(f"El precio actual del producto {product['nameProduct']} es de : ${product['priceProduct']:.2f}.")
                option1 = input(f"Esta seguro que desea {txtOption} el producto {product['nameProduct']}? \nIngrese 1: Para {txtOption} o Ingrese: Cualquier tecla para volver al menu:")
                if option1 == "1":
                    print(f"")
                    product["priceProduct"]= valueValidation("el nuevo precio del producto en UNDS: $")
                    print(f"El producto {product['nameProduct']} se ha modificado correctamente.\n")
                    print(f"El nuevo precio del producto es ${product['priceProduct']:.2f}.") 
                    return
                else:
                    print(f"No se {txtOption} el producto.\n")
                    return            
            else: #Here its executed the fourth option (Delete product)
                option1 = input(f"Esta seguro que desea {txtOption} el producto {product["nameProduct"]}? \n\nIngrese 1: Para {txtOption} o Ingrese: Cualquier tecla para volver al menu:")
                if option1 == "1":
                    productInventoryList.remove(product)
                    print(f"\n¡¡¡El producto {product['nameProduct']} se ha eliminado correctamente!!!\n")
                    return
                else:
                    print(f"No se {txtOption} el producto.\n")
                    return
    print(f"\n¡¡¡El producto {nameProduct} no se ha encontrado en el inventario!!!")     
        
#This function is used to calculate the price about all inventory
def valueInventory ():
    valueProducts = []
    if len(productInventoryList) ==  0:
        print("Primero debe agregar productos para realizar cualquier otra acción: \n")
        addProduct()
        return
    for product in productInventoryList:
        print(f"Producto: {product['nameProduct']} | Precio: ${product['priceProduct']:.2f} | Cantidad: {product['productQuantity']} | Precio total: {multiplyProduct(product['priceProduct'],product['productQuantity']):.2f}")
        valueProducts.append(multiplyProduct(product["priceProduct"],product["productQuantity"]))
    print(f"\nEl valor total del inventario es de: ${sum(valueProducts):.2f}")
        
#This function is used to validate the menu options
def main ():
    while True:
        menu()
        try:
            option = int(input("Ingrese opcion: "))
            match option:
                case 1:
                    addProduct()
                case 2:
                    print("-"*10,"Busqueda de producto","-"*10,"\n")
                    searchModifyOrDeleteProduct(option,"buscar")
                case 3:
                    print("-"*10,"Modificación de producto","-"*10,"\n")
                    searchModifyOrDeleteProduct(option,"modificar")
                case 4:
                    print("-"*10,"Eliminar producto","-"*10,"\n")
                    searchModifyOrDeleteProduct(option,"eliminar")
                case 5:
                    print("\n","-"*13,"Valor total del inventario","-"*13,"\n")
                    valueInventory()
                case 6:
                    print("\n","-"*13,"Fin del programa","-"*13,"\n")
                    break
                case _:
                    print("\n¡¡¡Ingeso una opción incorrecta.!!!")
        except ValueError:
            print("¡¡¡Ingreso un valor no numerico.!!!")
                      
main()