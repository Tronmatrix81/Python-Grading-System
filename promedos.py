from extras import students
import studentsearch
matricula=0
aux1=0
aux2=0
queso=""
nombres=(0,0)

def saved(mat: int):
    studentsearch.FindStudent
    print("Insert your Student ID")
    matricula=int(input())
    print(studentsearch.FindStudent(matricula))
    aux1=matricula
    
    queso=students.get(aux1,"Student not found!")
    quesoo=queso
    if queso == "Student not found!":
        return
    else:
        promedio()


def promedio():
    casos=int(input("Do you want to calculate just one subject or all your subjects?" \
    " 1- JUST ONE SUBJECT" \
    " 2- ALL SUBJECTS "))
    
    match casos:
        case 1:
            materia=input("What is the name of the subject that you want to calculate the average?")
            p1=int(input("What is the grade that you got in your first partial? "))
            p2=int(input("What is the grade that you got in your second partial? "))
            p3=int(input("What is the grade that you got in your third partial? "))
            prom=((p1*0.3)+(p2*0.3)+(p3*0.4))
            rep=0
            apro=0
            print("Your average in ", materia," is: ", prom )
            if prom <7:
                rep+=1
                print("You have failed this subject")
            if prom <10 and prom >=7:
                apro+=1
                print("You have passed this subject!")


        case 2:  #necesito total reprobadas, aprobadas y total de materias en dif variables
            subjects=int(input("How many subjects do you have in total?"))
            aux2=subjects
            if subjects >12 or subjects<2:
                print("The ammount of subjects is less or more than the necessary to continue.")
            else:
                subjects=0
                for i in range(aux2):
                    materia=input("What is the name of the subject that you want to calculate the average?")
                    p1=int(input("What is the grade that you got in your first partial? "))
                    p2=int(input("What is the grade that you got in your second partial? "))
                    p3=int(input("What is the grade that you got in your third partial? "))
                    prom=((p1*0.3)+(p2*0.3)+(p3*0.4))
                    rep=0
                    apro=0
                    print("Your average in ", materia," is: ", prom )
                    if prom <7:
                        rep+=1
                        print("You have failed this subject")
                    if prom <10 and prom >=7:
                        apro+=1
                        print("You have passed this subject!")

        


            

saved(mat=1)
