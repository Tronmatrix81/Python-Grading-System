import os
from team import students


def FindStudent(num: int)-> str:
    return students.get(num, "Student not found!")

def SearchForStudent():
    os.system("cls")
    print("Type in a student ID: ")
    id = int(input())
    print(FindStudent(id), "\n")
    os.system('pause')