# 

print("Adivina el numero: ")
print("Debe de adivinar el numero que esta pensando el sistema del 0 al 100 ")
import random

randomNum = random.randint(1,100)

def requestNum():
    while True:
        try:
            num = int(input("Ingrese un numero del 0 al 100: "))
            while not(0 <= num <= 100):
                num = int(input("Debe ingresar un numero del 0 al 100: "))
            return num
        except ValueError:
            print("Ingre un valor en numeros enteros: ")

number = requestNum()
cont= 1
while number != randomNum:
    if number > randomNum:
        print("El numero ingresado es MENOR, Ingrese otro numero:")
        number=requestNum()
    else:
        print("El numero es MAYOR, ingrese otro numero: ")
        number=requestNum()
    cont=cont+1

print ("Correcto, El numero del sistema es: ",randomNum)
print ("Numero de intentos: ", cont)

