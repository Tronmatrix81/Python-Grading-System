import os
from extras import students
from ekzel import read_cell

def print_credits():
    # Clear screen
    os.system("cls")

    print("~~ MIEMBROS DE TRANZIT ~~\n")
    for id in students:
        print(f"  > {students[id]}")

    print()
    os.system("pause")

def print_credits1():
    os.system("cls")

    print("~~ MIEMBROS DE TRANZIT ~~\n")
    for i in range(3):
            print(f"  > {read_cell(i+2, 2)}")

    print()
    os.system("pause")