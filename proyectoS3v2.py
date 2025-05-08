# Inventario de productos
print("="*10,"Inventario de productos","="*10)

products = []

def requestOption():
    while True:
        try:
            option = int(input("Ingrese opcion: "))
            while not(0 < option <7):
                option = int(input("Ingrese opcion del 1 al 6: "))
            return option
        except ValueError:
            print("Debe ingresar una opcion numerica: ")
            
# para validar que los datos de precio y cantidad sean positivos   
def valueValidation (cantValue):
    while True:
        try:
            value = int(input(f"Ingrese {cantValue}"))
            while value < 0:
                value = int(input(f"Error: Ingrese {cantValue}"))
            return value
        except ValueError:
            print (f"Error: {cantValue} debe ser en numeros.")
            
   
def addProduct ():
    while True:
        productName = input("Ingrese el nombre del producto: ").strip()
        while productName == "":
            productName = input("Error: Ingrese el nombre del producto: ").strip()
        productQuantity = valueValidation("Cantidad del producto: ")
        productPrice = valueValidation ("Precio del producto en UND: ")
        products.append({"product": productName, "quantity":productQuantity, "price":productPrice})
        option = input("\nIngrese 1: Para ingresar mas productos. \nIngrese: Cualquier tecla para salir. \n")
        if option == "1":
            print("\n")
            continue
        else:
            print ("\n")
            break


def iterateProducts (option,iterate):
    if len(products) == 0:
        print("Aun no se ha ingresado ningun producto al inventario, por favor añada productos.\n")
    else:
        iterateProduct = input(f"Ingrese el producto que desea {iterate}: ").strip()
        while iterateProduct == "":
            iterateProduct = input(f"Error: El campo no puede estar vacio. Ingrese el producto que desea {iterate}: ").strip()
        for product in products:
            if product["product"] == iterateProduct:
                print(f"El producto {iterateProduct} se ha encontrado: ")
                if option == 2:
                    print(f"Cantidad del producto {iterateProduct}: {product["quantity"]}")
                    print(f"Precio del producto {iterateProduct}: ${product["price"]}\n")
                    return
                elif option == 3:
                    product["price"] = valueValidation("Ingrese el nuevo precio del producto: $")
                    print("Precio modificado correctamente \n")
                    return
                else:
                    products.remove(product)
                    return
                #break
        print(f"\n El producto {iterateProduct} no encontrado en el inventario.\n")

multiplyValueProduct = lambda x , y : x*y

def valueInventory ():
    valueInventoryByProducts = []
    for product in products:
        valueInventoryByProduct = multiplyValueProduct(product["quantity"],product["price"])
        valueInventoryByProducts.append(valueInventoryByProduct)
    print(f"El valor total del inventario es: ${sum(valueInventoryByProducts)}\n")

def main ():
    
    while True:
        print("------------------- Menu --------------------\n")
        print("Digite el numero para las siguientes opciones: \n\n 1: Añadir producto.  \n 2: Consultar productos. \n 3: Actualizar precios. \n 4: Eliminar producto. \n 5: Calcular valor del inventario.\n 6: Salir \n")
        print("---------------------------------------------\n")
        option = requestOption()
        if option == 1:
            print("-"*10,"Añadir nuevo producto","-"*10,"\n")
            addProduct()
            print (products)
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
#enviar el parametro option de el main para ejecutar otras tareas en otra clase 

main ()
print(products)

#en cada paso validar si la lista ya contiene valores 