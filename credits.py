import os
from extras import students

def print_credits():
    # Clear screen
    os.system("cls")

    print("~~ MIEMBROS DE TRANZIT ~~\n")
    for id in students:
        print(f"  > {students[id]}")

    print()
    os.system("pause")