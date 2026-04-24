
from team import students
from studentsearch import SearchForStudent
cant=(int(input("How many subjects do you have?")))
if cant<2 or cant>12:
    print("You have more than the maximum or less than the minimum of subjects that you can have in one semester")
else:
    aux=0
    aux=cant
    cant=1
    print(aux)
    while(True):
        print(cant)
        print(aux)
        materia=(input("Type the subject that you want to get the average "))
        p1=(int(input("How much score did you get in your first partial? ")))
        p2=(int(input("How much score did you get in your second partial? ")))
        p3=(int(input("How much score did you get in your third partial? ")))
        print("Your average is: ",((p1*0.3)+(p2*0.3)+(p3*0.4)))
        
        if cant==aux:
            break
        cant += 1

        