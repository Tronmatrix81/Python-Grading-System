import os
from pick import pick #Python library
from studentsearch import search_for_student
from extras import menuOptions
from credits import print_credits

def menu():
    os.system('cls')
    print("UACH Grading System")
    for i in range(0, len(menuOptions)):
        print(menuOptions[i])    

    try:
        option = int(input("\nOption: "))
    except ValueError:
        print("Error: Not a number.\n")
        os.system("pause")
        menu()
    else:
        match option:
            case 1:
                search_for_student()
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

def menu2():
    title = "UACH Grading System"
    indicator = ">" #This is the cursor
    index = pick(menuOptions, title, indicator) #Gives two arguments (selected option and selected index)
    match index[1]:
        case 0:
            search_for_student()
        case 1:
            pass
        case 2:
            pass
        case 3:
            print_credits()
        case 4:
            return
    menu2()

if __name__=="__main__": menu2()