import os
from pick import pick #Python library

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
        match index[1]:
            case 0:
                search_for_student()
            case 1:
                saved(mat=1)

            case 2:
                exam_check()
                
            case 3:
                print_credits()
            case 4:
                return
        menu()

if __name__=="__main__": menu()