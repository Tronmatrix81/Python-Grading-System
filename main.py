import os
from pick import pick #Python library
from ekzel import add_member_ui, remove_member_ui
from promedios import saved
from studentsearch import search_for_student
from exam_check import exam_check
from extras import menu_options
from credits import print_credits

def menu():
    title = "~~UACH Grading System~~"
    indicator = ">" #This is the cursor
    try:
        index = pick(menu_options, title, indicator) #Gives two arguments (selected option and selected index)
    except KeyboardInterrupt:
        print("Program interrupted")
    else:
        os.system('cls')
        match index[1]:
            case 0:
                search_for_student()
            case 1:
                saved()
            case 2:
                exam_check()
            case 3:
                add_member_ui()
                pass
            case 4:
                remove_member_ui()
                pass
            case 5:
                print_credits()
            case 6:
                os.system('cls')
                if input("Are you sure you want to exit? (y/n): ").strip().lower() == 'y':
                    print("See you later!")
                    exit()
        menu()

if __name__=="__main__": menu()