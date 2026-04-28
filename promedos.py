from extras import students
import studentsearch
matricula=0
aux1=0
aux2=0
nombres=(0,0)
def saved(mat: int):
    studentsearch.FindStudent
    print("Insert your Student ID")
    matricula=int(input())
    print(studentsearch.FindStudent(matricula))
    aux1=matricula
    print(aux1)
    queso=students.get(aux1,"hola")
def promedio():
    subjects=int(input("How many subjects do you have? "))
    aux2=subjects
    #necesito total reprobadas, aprobadas y total de materias en dif variables
    if subjects >12 or subjects<2:
        print("The ammount of subjects is less or more than the necessary to continue.")
    else:
        subjects=0
        for i in range(aux2):

            

saved(mat=1)
promedio()