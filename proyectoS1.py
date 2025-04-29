#calculadora de productos
#Este programa calcula el valor total de una compra, aplicando un descuento si corresponde.
#El programa solicita al usuario el nombre del producto, el precio, la cantidad y el porcentaje de descuento.
#El programa valida que los datos ingresados sean correctos y muestra el resultado final.

print("Calculadora de productos: ") #Imprimir un titulo

ingresar = 1

#Recopilación de datos 
#solicitamos el nombre del producto 
nombreProducto= input("Ingrese el nombre del producto: ")
while nombreProducto == "": #hacemos un while si no ingresan el nombre del producto 
    nombreProducto= input("Error: Ingrese el nombre del producto: ")

#validación del precio producto
while True: #hacemos un bucle hasta que se ingrese un valor correcto en el precio del producto  
    try: #hacemos un try para que no salga un error si se ingresan letras 
        valorProducto= float(input("Por favor ingrese el precio del producto: $"))
        while valorProducto < 0  : #hacemos un bucle para validar que no ingrese un valor negativo
            valorProducto= float(input("Error: Por favor ingrese el precio del producto: $"))
        break #El break se usa para romper el ciclo del while true
    except ValueError : #Esta lina se ejecuta si en el try se produce un error del tipo valueError (se ejecuta cuando la entrada del usuario no se puede convertir a float)
            print("Error: Por favor ingrese el precio en numeros")

#validación de la cantidad de productos
while True:
    try:
        cantidadProducto= int(input("Ingrese la cantidad del producto: "))
        while cantidadProducto <= 0 :
             cantidadProducto= int(input("Error: Ingrese la cantidad del producto: "))
        break 
    except ValueError :
        print("Error: Por favor ingrese la cantidad deproductos en numeros")
    
#validación de porcentaje
while True:
    try:
        porcentajeDescuento= float(input("Ingrese el Porcentaje del descuento del producto: "))
        while porcentajeDescuento < 0 or porcentajeDescuento > 100:
             porcentajeDescuento= float(input("Ingrese el Porcentaje del descuento del producto: "))
        break
    except ValueError:
        print("Error: Debe ingresar un numero:")





print("Producto: ",nombreProducto , "| Valor Producto: $", valorProducto,"| Cantidad: ",cantidadProducto,"UND")     #Imprimo el nombre del producto, el valor y cantidad  


valorCompra= valorProducto*cantidadProducto #calculo el valor total de la compra
valorCompraPorcentaje= (porcentajeDescuento/100)*valorCompra #calculo el descuento
valorTotal=valorCompra-valorCompraPorcentaje #calculo el valor total de la compra con descuento

#imprimo los valores
print(f"Valor: ${valorCompra:.2f}")
print(f"Valor Descuento: ${valorCompraPorcentaje:.2f}")
print(f"Valor a pagar: ${valorTotal:.2f}") 

