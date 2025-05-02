# calificaciones


print("---------------------SISTEMA DE CALIFICACIONES---------------------- \n")

def requesOption():
    print("------------------- Menu --------------------\n")
    print("Digite el numero para las siguientes opciones: \n\n 1: Determinar estado de aprobación.  \n 2: Calcular el promedio de calificaciones. \n 3: Contar cantidad de calificaciones mayores. \n 4: Verificar y contar calificaciones específicas. \n 5: Salir.\n")
    print("---------------------------------------------\n")
    while True:
        try:
            option = int(input("Ingrese opcion: "))
            while not(0 < option <6):
                option = int(input("Ingrese opcion del 1 al 5: "))
            return option
        except ValueError:
            print("Debe ingresar una opcion numerica: ")

def valueValidation ():
    value = 0
    while True:
        try:
            value = int(input("Ingrese un valor de 0 a 100: "))
            while not ( 0 <= value <= 100):
                value = int(input("Ingrese un valor de 0 a 100: "))
            return value
        except ValueError:
            print("Debe ingresar un valor numerico de 0 a 100: ")


def gradesComparison ():
    print("--------------Validación de aprobación-----------------\n")
    minimunGrade  =  60
    while True:
        print("Ingrese  una calificación: ")
        grade  =  valueValidation()
        if grade < minimunGrade:
            print("Reprobado")
        else:
            print("Aprobado")
        cont = input("desea ingresar mas calificaciones? 1=si 0=no:")
        if cont == "1":
            continue
        else:
            print("\n")
            break

gradesList = []

def requestGrades():
    grades = input ("Ingrese las calificaciones seperadas por comas (,): ").split(",")  
    for i in grades:
        try:
            floatGrades = float(i.strip())
            if 0 <= floatGrades <= 100:
                gradesList.append(floatGrades)
            else:
                print(f"Error: el valor {i.strip()} no es un valor de 0 a 100, sera omitido")
        except ValueError: 
            print(f"Error: el valor {i.strip()} sera omitido")
    
def gradesAverage():
    print("------------- Promedio de las notas------------------\n")
    requestGrades()
    gradesAdd = sum(gradesList)
    gradesAvg = gradesAdd/len(gradesList)
    print (f"La suma total de las {len(gradesList)} calificaciones es de: {gradesAdd:.2f}")
    print (f"El promedio de las {len(gradesList)} calificaciones es de: {gradesAvg:.2f}\n")

def higherGrades():
    print("-------------- Calificaciones Mayores ----------------\n")
    if len(gradesList) == 0:
        print("Primero debe ingresar una lista de calificaciones. ")
        requestGrades()
    cont=0
    cont1=0
    hGrades=[]
    print("Ingrese una calificación para contar las mayores:")
    grade = valueValidation()
    while cont < len(gradesList):
        validationGrade=gradesList[cont]
        if grade < validationGrade:
            cont1 += 1
            hGrades.append(validationGrade)
        cont += 1
    print(f"La cantidad de notas mayores a {grade} son: {cont1}")
    print(f"Las calificaciones mayores a {grade} son: {hGrades:.2f}\n")

def conterGrades ():
    print("--------------------- Contador de calificaciones ---------------\n")
    if len(gradesList) == 0:
        print("Primero debe ingresar una lista de calificaciones. ")
        requestGrades()
    print("Ingrese una calificación para buscar cuantas mas hay.")
    cont=0
    grade = valueValidation()
    for i in gradesList:
        if grade == i:
             cont += 1
    print(f"Se encontraron {cont} calificaciones iguales a {grade}\n")

while True:
    option=requesOption()
    if option == 1:
        gradesComparison()
    elif option == 2:
        gradesAverage()
    elif option == 3:
        higherGrades()
    elif option == 4:
        conterGrades()
    else:
        break
