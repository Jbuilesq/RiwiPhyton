# request age

def requestAge ():
    try:
        age = int(input("Por favor ingrese la edad:"))
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
        requestAge()
        




requestAge()