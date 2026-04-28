import os
from extras import students

def exam_check():
    os.system("cls")
    subjectNumber = [[0, 0], [0, 0], [0, 0]] # ID, total subjects, failed subjects
    print("~~Non-ordinary exam check~~")

    i = 0
    while i<len(students):
        print(f"\n{students[list(students)[i]]}:")
        try:
            subjectNumber[i][0]=int(input("How many subjects do you take? "))
            if not (2<subjectNumber[i][0]<12):
                print("Error: Too many or too few subjects.")
                pass

            subjectNumber[i][1]=int(input("How many subjects are you failing? "))
            if not (0<=subjectNumber[i][1]<=subjectNumber[i][0]):
                print("How is that even possible?")
                pass

        except ValueError:
            print("Error: Not a number.")
            pass

        i += 1

    i = 0
    while i<len(students):

        approved = 0
        if (subjectNumber[i][0]/2)+1>(subjectNumber[i][1]):
            approved = 1
        decision = "has right" if approved==1 else "doesn't have right"

        print(f"\n{students[list(students)[i]]} {decision} to take the exam")
        i += 1

    os.system("pause")