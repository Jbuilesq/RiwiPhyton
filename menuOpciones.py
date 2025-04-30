print("-----------Menu De Opciones-------------- \n")


def ages ():
    try:
        age = int(input("Por favor ingrese la edad:"))
        while age < 0:
            age = int(input("Por favor ingrese la edad en numeros enteros positivos:"))
        if age < 12:
            print("Eres un niño")
        elif 12 <= age <= 17:
            print("Eres un adolecente")
        elif 17 < age < 60:
            print("Eres Adulto")
        else:
            print("Eres un adulto mayor")
    except ValueError:
        print("Digita la edad en numeros")
        ages()

def requesOption():
    print("Digite el numero para las siguientes opciones: \n 1: Saludar \n 2: Decir edad \n 3: Salir \n")
    while True:
        try:
            option = int(input("Ingrese opcion: "))
            while not(0 < option <4):
                option = int(input("Ingrese opcion del 1 al 3: "))
            return option
        except ValueError:
            print("Debe ingresar una opcion numerica: ")

while True:
    option=requesOption()
    if option == 1:
        print("Bienvenido: \n")
    elif option == 2:
        ages()
    else:
        break


print ("Gracias por usar nuestro programa")
    

