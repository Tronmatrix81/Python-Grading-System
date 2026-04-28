import os
from extras import students

def print_credits():
    # Clear screen
    os.system("cls")

    print("~~ MIEMBROS DE TRANZIT ~~\n")
    for student in students:
        print(f"  > {students[student]}")

    print()
    os.system("pause")