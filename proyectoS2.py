# sistema de calificaciones
# El programa permite ingresar calificaciones y realizar diferentes operaciones como determinar el estado de aprobación, calcular el promedio, contar calificaciones mayores a un valor específico y verificar cuántas veces aparece una calificación específica.


print("---------------------SISTEMA DE CALIFICACIONES---------------------- \n")
#requestOption es una funcion donde se ejecuta un menu de opciones para el usuario. se valida que la opcion ingresada sea correcta.
def requestOption():
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
# valueValidation es una funcion para validar el valor de la calificacion ingresada por el usuario.
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

# gradesComparison es una funcion que valida si la calificacion ingresada es mayor o igual a 60, si es asi el alumno aprueba, si no reprobado.
def gradesComparison ():
    print("--------------Validación de aprobación-----------------\n")
    minimunGrade  =  60
    while True:
        print("Ingrese  una calificación: ")
        grade  =  valueValidation()# llama a la funcion valueValidation para validar el valor de la calificacion ingresada.
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

gradesList = []# se declara una lista global para usarla en diferentes funciones.
#requestGrades es una funcion que solicita al usuario ingresar las calificaciones, las valida y las agrega a la lista gradesList.
def requestGrades():
    grades = input ("Ingrese las calificaciones seperadas por comas (,): ").split(",")  #con el split se separan las calificaciones ingresadas por el usuario.
    for i in grades:
        try:
            floatGrades = float(i.strip())# se convierte el valor ingresado a float y se eliminan los espacios en blanco.
            if 0 <= floatGrades <= 100:
                gradesList.append(floatGrades)# se agrega el valor a la lista gradesList.
            else:
                print(f"Error: el valor {i.strip()} no es un valor de 0 a 100, sera omitido")
        except ValueError: 
            print(f"Error: el valor {i.strip()} sera omitido")
#gradesAverage es una funcion que calcula el promedio de las calificaciones ingresadas por el usuario.    
def gradesAverage():
    print("------------- Promedio de las notas------------------\n")
    requestGrades()
    gradesAdd = sum(gradesList)#con sum() se suman todos los valores de la lista gradesList.
    gradesAvg = gradesAdd/len(gradesList) #con len() se obtiene la cantidad de elementos de la lista y se divide la suma total entre la cantidad de elementos para obtener el promedio.
    print (f"La suma total de las {len(gradesList)} calificaciones es de: {gradesAdd:.2f}")
    print (f"El promedio de las {len(gradesList)} calificaciones es de: {gradesAvg:.2f}\n")
#higherGrades es una funcion que cuenta cuantas calificaciones son mayores a la ingresada por el usuario.
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
#conterGrades es una funcion que cuenta cuantas veces aparece una calificacion especifica en la lista gradesList.
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

#while True: es un bucle infinito que ejecuta el menu de opciones hasta que el usuario decida salir.
while True:
    option=requestOption() #llama a la funcion requestOption para mostrar el menu de opciones.
    if option == 1:
        gradesComparison() #llama a la funcion gradesComparison para ejecutar la validacion de aprobacion.
    elif option == 2:
        gradesAverage() #llama a la funcion gradesAverage para ejecutar el calculo del promedio.
    elif option == 3:
        higherGrades() #llama a la funcion higherGrades para ejecutar el conteo de calificaciones mayores.
    elif option == 4:
        conterGrades() #llama a la funcion conterGrades para ejecutar el conteo de calificaciones especificas.
    else:
        break #si el usuario ingresa 5 u otra opcion diferente a las anteriores, se sale del bucle y termina el programa.

print("Gracias por usar el sistema de calificaciones. \n")
print("Fin del programa. \n")
