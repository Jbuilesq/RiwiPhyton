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
    print("-"*10,"Añadir producto","-"*10,"\n")
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

def searchProducts ():
    search = input("Ingrese el producto que desea consultar: ").strip()
    while search == "":
        search = input("Error: El campo no puede estar vacio. Ingrese el producto que desea consultar: ").strip()
    for product in products:
        if product["product"] == search:
            print(f"El producto {search} se ha encontrado: ")
            print(f"Cantidad del producto {search}: {product["quantity"]}")
            print(f"Precio del producto {search}: ${product["price"]}")
            break

def main ():
    
    while True:
        print("------------------- Menu --------------------\n")
        print("Digite el numero para las siguientes opciones: \n\n 1: Añadir producto.  \n 2: Consultar productos. \n 3: Actualizar precios. \n 4: Eliminar producto. \n 5: Calcular valor del inventario.\n 6: Salir \n")
        print("---------------------------------------------\n")
        option = requestOption()
        if option == 1:
            addProduct()
        elif option == 2:
            searchProducts()
        elif option == 3:
            print("actualizar precio producto")
        elif option == 4:
            print("Eliminar Producto")
        elif option == 5:
            print("calcular valor inventario")
        else:
            break
        
        

main ()
print(products)

#en cada paso validar si la lista ya contiene valores 