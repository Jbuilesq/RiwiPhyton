# PRODUCTS INVENTORY
print("="*10,"Inventario de productos","="*10)

#products list is declared global to use on others function
products = []

#requestOption is a function to validate the input option to menu 
def requestOption():
    while True:
        try:
            option = int(input("Ingrese opcion: "))
            while not(0 < option <7):
                option = int(input("Ingrese opcion del 1 al 6: "))
            return option
        except ValueError:
            print("Debe ingresar una opcion numerica: ")
            
#Value validation is a function to validate quantity and value inputs are numbers and positives 
def valueValidation (cantValue):
    while True:
        try:
            value = int(input(f"Ingrese {cantValue}"))
            while value < 0:
                value = int(input(f"Error: Ingrese {cantValue}"))
            return value
        except ValueError:
            print (f"Error: {cantValue} debe ser en numeros.")
            
#This function add procduts to products list 
def addProduct ():
    while True:
        productName = input("Ingrese el nombre del producto: ").lower().capitalize().strip()
        while productName == "":
            productName = input("Error: Ingrese el nombre del producto: ").lower().capitalize().strip()
        for product in products:
            if product["product"] == productName:
                print("El producto ya existe\n")
                return
        productQuantity = valueValidation("Cantidad del producto: ")
        productPrice = valueValidation ("Precio del producto en UND: $")
        products.append({"product": productName, "quantity":productQuantity, "price":productPrice})
        option = input("\nIngrese 1: Para ingresar mas productos O Ingrese: Cualquier tecla para volver al menu: ")
        if option == "1":
            continue
        else:
            break

# this function search the product if the product is found show the information product (Quantity and price), modify price or remove product from products list. 
def iterateProducts (option,iterate): # receive two variables: option(to select what i whant to do whit the product) and iterate(to display interactive messages)
    if len(products) == 0: #here validate if list is empty
        print("Aun no se ha ingresado ningun producto al inventario, por favor añada productos.\n")
    else:
        iterateProduct = input(f"Ingrese el producto que desea {iterate}: ").lower().capitalize().strip()
        while iterateProduct == "":
            iterateProduct = input(f"Error: El campo no puede estar vacio. Ingrese el producto que desea {iterate}: ").lower().capitalize().strip()
        for product in products:
            if product["product"] == iterateProduct:
                print(f"El producto {iterateProduct} se ha encontrado: ")
                if option == 2: # here we show price and quintity of product 
                    print(f"Cantidad del producto {iterateProduct}: {product["quantity"]}")
                    print(f"Precio del producto {iterateProduct}: ${product["price"]}\n")
                    return
                elif option == 3:# here we can update the price
                    product["price"] = valueValidation("Ingrese el nuevo precio del producto: $")
                    print("Precio modificado correctamente \n")
                    return
                else: #and here we can remove products from  products list (inventory)
                    option1 = input(f"Esta seguro que desea eliminar el producto {product["product"]}? \nIngrese 1: Para eliminar o Ingrese: Cualquier tecla para volver al menu:")
                    if option1 == "1":
                        products.remove(product)
                        print(f"El producto {product["product"]} se ha eliminado correctamente.\n")
                        return
                    else:
                        print("No se elimino el producto.\n")
                        return
        print(f"\n El producto {iterateProduct} no encontrado en el inventario.\n")

#here we multiply he price about each product by its quantity 
multiplyValueProduct = lambda x , y : x*y

#this function stores the total price of product and calculate the value of inventory
def valueInventory ():
    valueInventoryByProducts = []
    for product in products:
        valueInventoryByProduct = multiplyValueProduct(product["quantity"],product["price"])
        print(f"Producto {product["product"]}: Cantidad: {product["quantity"]} UNDS. Precio: ${product["price"]}. Total: {valueInventoryByProduct}")
        valueInventoryByProducts.append(valueInventoryByProduct)
    print(f"\nEl valor total del inventario es: ${sum(valueInventoryByProducts)}\n")

# main is a function where the menu is executed
def main ():
    
    while True:
        print("------------------- Menu --------------------\n")
        print("Digite el numero para las siguientes opciones: \n\n 1: Añadir producto.  \n 2: Consultar productos. \n 3: Actualizar precios. \n 4: Eliminar producto. \n 5: Calcular valor del inventario.\n 6: Salir \n")
        print("---------------------------------------------\n")
        option = requestOption()
        if option == 1:
            print("-"*10,"Añadir nuevo producto","-"*10,"\n")
            addProduct()
        elif option == 2:
            print("-"*10,"Busqueda de producto","-"*10,"\n")
            iterateProducts(option,"buscar")
        elif option == 3:
            print("-"*10,"Modificación de producto","-"*10,"\n")
            iterateProducts(option,"modificar")
        elif option == 4:
            print("-"*10,"Eliminar producto","-"*10,"\n")
            iterateProducts(option,"eliminar")
        elif option == 5:
            valueInventory()
        else:
            break
    print("\n","-"*13,"Fin del programa","-"*13,"\n")

main ()
#print(products)
