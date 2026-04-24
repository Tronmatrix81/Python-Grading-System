import os
from team import students

# Clear screen
os.system("cls")

print("\t~~ MIEMBROS DE TRANZIT ~~\n")
for student in students:
    print(f"\t{students[student]}\n")