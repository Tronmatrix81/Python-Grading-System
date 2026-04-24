import os
from extras import students

def print_credits():
    # Clear screen
    os.system("cls")

    print("\t~~ MIEMBROS DE TRANZIT ~~\n")
    for student in students:
        print(f"\t{students[student]}\n")

    os.system("pause")