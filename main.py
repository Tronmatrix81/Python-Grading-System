import os
import studentsearch
from credits import print_credits
menuCommands = ["1)\tSearch Student ID", "2)\tGrades and promedy", "3)\tNon-odrinary check", "4)\tCredits"]
    
def menu():
    os.system('cls')
    print("UACH Grading System")
    for i in range(0, len(menuCommands)):
        print(menuCommands[i])    

    try:
        option = int(input("\nOption: "))
    except ValueError:
        print("Error: Not a number.\n")
        os.system("pause")
        menu()
    else:
        match option:
            case 1:
                studentsearch.SearchForStudent()
            case 2:
                pass
            case 3:
                pass
            case 4:
                print_credits()
            case _:
                print("Invalid argument.")
                os.system("pause")
        menu()

if __name__=="__main__": menu()