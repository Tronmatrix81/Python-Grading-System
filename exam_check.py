import os
from extras import students
from ekzel import write_cell
from ekzel import max_row
from ekzel import read_cell

def exam_check():
    os.system("cls")
    subjectNumber = [[0, 0], [0, 0], [0, 0]]
    print("~~Non-ordinary exam check~~")

    i=0
    while i<len(students):

        # Prints current student name
        print(f"\n{students[list(students)[i]]}:")

        # Total subjects loop
        while True:
            try:
                subjectNumber[i][0]=int(input("How many subjects are you taking? "))
                if not (2<=subjectNumber[i][0]<=12):
                    print("Error: Too many or too few subjects.\n")
                    continue

                break

            except ValueError:
                print("Error: Not a number.")

        # Failed subjects loop
        while True:
            try:
                subjectNumber[i][1]=int(input("How many subjects are you failing? "))
                if not (0<=subjectNumber[i][1]<=subjectNumber[i][0]):
                    print("Error: How is that even possible?\n")
                    continue

                break

            except ValueError:
                print("Error: Not a number.\n")

        i += 1

    i=0
    while i<len(students):

        isApproved=0
        if ((subjectNumber[i][0]/2)+1)>(subjectNumber[i][1]):
            isApproved=1

        decision= "has right" if isApproved==1 else "doesn't have right"

        print(f"\n{students[list(students)[i]]} {decision} to take the exam")
        write_cell(i+2, 7, decision)
        i += 1

    os.system("pause")


def exam_check_v2():
    os.system("cls")

    students = []
    totalHours = 0
    absences = 0
    totalSubjects = 0
    failedSubjects = 0

    for i in range(2, max_row("promedio")+1):
        students.append([read_cell("promedio", i, 2)])

    # Function start
    print("~~Non-ordinary exam check: Calculus~~")

    try:
        totalHours=16*(int(input("\nHow many hours (weekly) is your subject? ")))
        if not (0<=totalHours):
            print("Error: How is that even possible?")
    except ValueError:
        print("Error: Not a number.")
    
    i=0
    while i<len(students):

        # Current student
        print(f"\n{students[i][0]}:")

        # Assists loop
        while True:
            try:
                absences=int(input("How many absences do you have in total? "))
                if not (0<=absences<=totalHours):
                    print("Error: Too many or too few absences.\n")
                    continue
                break
            except ValueError:
                print("Error: Not a number.")

        if ((absences)<(totalHours*0.6)):
            while True:
                try:
                    totalSubjects=int(input("How many subjects do you take? "))
                    if not (0<=totalSubjects<=12):
                        print("Error: too many or too few subjects")
                        continue
                    break
                except ValueError:
                    print("Error: Not a number.")

            while True:
                try:
                    failedSubjects=int(input("How many subjects did you fail? "))
                    if not (0<=failedSubjects<=totalSubjects):
                        print("Error: How is that even possible?")
                        continue
                    break
                except ValueError:
                    print("Error: Not a number.")

            if (failedSubjects)<(totalSubjects*0.5):
                students[i].append("has right")
            else:
                students[i].append("doesn't have right")
            
        else:
            students[i].append("doesn't have right")

        i += 1

    os.system("cls")
    for i in range(len(students)):
        print(f"\n{students[i][0]} {students[i][1]} to take the exam.")
        write_cell(i+2, 8, students[i][1])

    os.system("pause")