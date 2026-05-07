import os
import openpyxl

excelFile = ""

def open_excel():
    global excelFile

    absolutePath=os.path.dirname(os.path.abspath(__file__))
    excelPath=os.path.join(absolutePath, "queso.xlsx")

    try:
        excelFile=openpyxl.load_workbook(excelPath)
    except:
        print("Error: File doesn't exist or is already open.")

    return

def write_excel():
    open_excel()