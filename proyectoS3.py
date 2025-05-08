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
            
#def productValidation ():    para validar los productos 
   
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

# def searchProducts ():
#     search = input("Ingrese el producto que desea consultar: ").strip()
#     while search == "":
#         search = input("Error: El campo no puede estar vacio. Ingrese el producto que desea consultar: ").strip()
#     for product in products:
#         if product["product"] == search:
#             print(f"El producto {search} se ha encontrado: ")
#             print(f"Cantidad del producto {search}: {product["quantity"]}")
#             print(f"Precio del producto {search}: ${product["price"]}\n")
#             break

# def changeValueProducts ():
#     search = input("Ingrese el producto que desea Modificar: ").strip()
#     while search == "":
#         search = input("Error: El campo no puede estar vacio. Ingrese el producto que desea Modificar: ").strip()
#     for product in products:
#         if product["product"] == search:
#             print(f"El producto {search} se ha encontrado: ")
#             # print(f"Cantidad del producto {search}: {product["quantity"]}")
#             # print(f"Precio del producto {search}: ${product["price"]}\n")
#             product["price"] = valueValidation("Ingrese el nuevo precio del producto: ")
#             break

def removeProduct ():
    search = input("Ingrese el producto que desea Eliminar: ").strip()
    while search == "":
        search = input("Error: El campo no puede estar vacio. Ingrese el producto que desea Eliminar: ").strip()
    for product in products:
        if product["product"] == search:
            print(f"El producto {search} se ha encontrado: ")
            products.remove(product)
            break

def iterateProducts (option,iterate):
    search = input(f"Ingrese el producto que desea {iterate}: ").strip()
    while search == "":
        search = input(f"Error: El campo no puede estar vacio. Ingrese el producto que desea {iterate}: ").strip()
    for product in products:
        if product["product"] == search:
            print(f"El producto {search} se ha encontrado: ")
            if option == 2:
                print(f"Cantidad del producto {search}: {product["quantity"]}")
                print(f"Precio del producto {search}: ${product["price"]}\n")
            elif option == 3:
                product["price"] = valueValidation("Ingrese el nuevo precio del producto: ")
                print("Precio modificado correctamente \n")
            else:
                products.remove(product)
            break

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
            iterateProducts(option,"eliminar")
        elif option == 5:
            print("calcular valor inventario")
        else:
            break

#enviar el parametro option de el main para ejecutar otras tareas en otra clase 

main ()
print(products)

#en cada paso validar si la lista ya contiene valores 