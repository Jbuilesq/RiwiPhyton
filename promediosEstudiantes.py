print("="*7,"Promedios de estudianes","="*7, "\n" )

students=[]

def gradeValidation ():
    grade = 0
    while True:
        try:
            grade = float(input("Ingrese un valor de 0 a 5: "))
            while not ( 0 <= grade <= 5):
                grade = float(input("Ingrese un valor de 0 a 5: "))
            return grade
        except ValueError:
            print("Debe ingresar un valor numerico de 0 a 5: ")

def addStudent ():
    print ("-"*7,"Información estaudiante","-"*7)
    student=input("Ingrese nombre del estudiante: ")
    while student == "":
         student=input("Error: Ingrese nombre del estudiante : ")
    grades = []
    for i in range (3):
        print (f"Ingrese la calificación #{i+1}: ")
        grade = gradeValidation ()
        grades.append(grade)
    students.append({"estudiante":student,"nota":grades})
    return student,grades
    

def gradesAverage (nameStudent,gradesStudent):
    print("\n-------- Promedios estudiante ---------\n")
    # for studentInfo in len(students):
    #     print(studentInfo)
    #     nameStudent = studentInfo["estudiante"]
    #     print(nameStudent)
    #     gradesStudent = studentInfo["nota"]
    #     print(gradesStudent)
    if gradesStudent:
        avgGrades = sum(gradesStudent) / len(gradesStudent)
        print(f"El promedio de {nameStudent} es: {avgGrades:.2f}")
    else:
        print(f"{nameStudent} no tiene calificaciones.")
    gradesComparison(avgGrades)



def gradesComparison (avgGrade):
    if avgGrade <= 3:
        print("Reprobado.\n")
    else:
        print("Aprobado.\n")
   

while True:
    student, grades = addStudent ()
    gradesAverage(student,grades)
    option=input("Desea ingresar mas estudiantes: 0 = SI - 1 = NO: ")
    if option != "0":
        break

print(students)
print(type(students))
print(students[0]["nota"])
print(students[0]["nota"][2])