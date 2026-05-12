import os
from extras import students
from ekzel import read_cell

def print_credits():
    # Clear screen
    os.system("cls")

    print("~~ MIEMBROS DE TRANZIT ~~\n")
    for i in range(3):
            print(f"  > {read_cell('credits', i+2, 1)}")

    print()
    os.system("pause")