import os
from extras import students
import studentsearch
matricula=0
aux1=0
aux2=0
queso=""
nombres=(0,0)

def saved(mat: int):
    try:
        os.system("cls")
        studentsearch.find_student
        print("Insert your Student ID")
        matricula=int(input())
        print(studentsearch.find_student(matricula))
        aux1=matricula
        
        queso=students.get(aux1,"Student not found!")
        if queso == "Student not found!":
            
            os.system("pause")
            return
    except ValueError:
        print("Error: Incorrect character")
        os.system("pause")
    else:
        promedio()


def promedio():
    try:
        os.system("cls")
        casos=int(input("Do you want to calculate just one subject or all your subjects?" \
        " 1- JUST ONE SUBJECT" \
        " 2- ALL SUBJECTS "))
        if casos <1 or casos>2:
            print("That option is not possible")
            os.system("pause")
        else:
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
                        os.system("pause")
                    if prom <10 and prom >=7:
                        apro+=1
                        print("You have passed this subject!")
                        os.system("pause")
                    if prom >10:
                        print("Thats too much score man, we cant accept it")
                        os.system("pause")
                    if prom <0:
                        print("Good luck next time bro")
                        os.system("pause")


                case 2:  #necesito total reprobadas, aprobadas y total de materias en dif variables
                    subjects=int(input("How many subjects do you have in total?"))
                    aux2=subjects
                    if subjects >12 or subjects<2:
                        print("The ammount of subjects is less or more than the necessary to continue.")
                        os.system("pause")
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
                                os.system("pause")
                            if prom <10 and prom >=7:
                                apro+=1
                                print("You have passed this subject!")
                                os.system("pause")
                            if prom >10:
                                print("Thats too much score man, we cant accept it")
                                os.system("pause")
                            if prom <0:
                                print("Good luck next time bro")
                                os.system("pause")
    except ValueError:
        print("Error: Incorrect character")
        os.system("pause")
                        
                        
                            
                            


            


            

