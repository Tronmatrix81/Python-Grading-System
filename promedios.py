import os
from pick import pick
from extras import students
import studentsearch
from ekzel import  write_cell
from ekzel import read_cell
from ekzel import conteo
matricula=0
aux1=0
aux2=0

nombres=(0,0)

def saved():
    global queso
    global aux1
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
        aux1=str(matricula)
        parcial()
renglones=conteo()

def parcial():
    try:                    
        materia=input("What is the name of the subject that you want to calculate the average? ")
        
        write_cell(1,3,f"Partial 1 {materia}")
        write_cell(1,4,f"Partial 2 {materia}")
        write_cell(1,5,f"Partial 3 {materia}")
        z=1
        i=0 
       
        while i ==0:
                
            print (z)
            pozole=read_cell("promedio",z+1,1)
            print (renglones)
            if  z== renglones: 
                i=5
                os.system("pause")
                break
                
                    
                
            else:
                pan=read_cell("promedio",z+1,2)
                print("User that is being calculated ", pan)
                p1=int(input("What is the grade that you got in your first partial? "))
                if p1 <0 or p1>10:
                    print("Incorrect grade")
                    continue
                    
                p2=int(input("What is the grade that you got in your second partial? "))
                if p2 <0 or p2>10:
                    print("Incorrect grade")
                    os.system("pause")
                    continue
                p3=int(input("What is the grade that you got in your third partial? "))
                if p3 <0 or p3>10:
                    print("Incorrect grade")
                    continue
                    
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
                

                if apro == 1:
                    global passed
                    passed="Yes"
                if rep == 1:
                    
                    passed="No"

                    
                    
                    return
                write_cell(z+1,3,p1)
                write_cell(z+1,4,p2)
                write_cell(z+1,5,p3)
                write_cell(z+1,6,prom)
                write_cell(z+1,7,passed)
            z+=1
    except ValueError:
        print("Error: Incorrect character")
        os.system("pause")
