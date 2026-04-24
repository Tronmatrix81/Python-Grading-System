import os
import studentsearch

menuCommands = ["1) Search Student ID", "2) Something"]
    
def menu():
    os.system('cls')
    print("UACH Grading System")
    for i in range(0, len(menuCommands)):
        print(menuCommands[i])

    try:
        option = int(input())
    except ValueError:
        menu()
    else:     
        match (option):
            case 1:
                studentsearch.SearchForStudent()
            case 2:
                print()
        menu()


if __name__=="__main__": menu()