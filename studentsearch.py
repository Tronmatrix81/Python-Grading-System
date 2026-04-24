import os
from extras import students


def find_student(num: int)-> str:
    return students.get(num, "Student not found!")

def search_for_student():
    os.system("cls")
    print("Type in a student ID: ")
    id = int(input())
    print(find_student(id), "\n")
    os.system('pause')