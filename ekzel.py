import os
import openpyxl

absolutePath=os.path.dirname(os.path.abspath(__file__)) # Find actual directory
excelPath=os.path.join(absolutePath, "queso.xlsx") # Find directory's excel

def open_excel():
    global excelFile, excelPath

    try:
        excelFile=openpyxl.load_workbook(excelPath)
        
    except:
        print("Error: File doesn't exist or is already open.")

    return excelFile

def write_excel():
    open_excel()

def add_member():
    return

def remove_member():
    return




















#excelpath es ela rchivo
#excelsheet es la hoja
#excelfile es el cos carpeta
#eso no impporta


def write_cell(row:float, column:float, data:str):
    global excelPath

    excelFile=open_excel()#abre el archivo
    excelSheet=excelFile["promedio"]
    excelSheet.cell(row, column, data)
    #celda segun row columna y el dato, ese es el orden pues

    try:
        excelFile.save(excelPath)
    except PermissionError:
        print("Error: Excel file is currently open.")

def add_member():
    global excelPath
    os.system("cls")

    excelFile=open_excel()
    excelSheet=excelFile["promedio"]

    print("~~Add member~~")
    excelSheet.append(input("\nType matricula: "), input("Type name: "))

    try:
        excelFile.save(excelPath)
    except PermissionError:
        print("Error: Excel file is currently open.")

    os.system("pause")

def remove_member():
    global excelPath
    os.system("cls")

    excelFile=open_excel()
    excelSheet=excelFile["promedio"]

    print("~~Remove member~~")
    excelSheet.append(input("\nType matricula: "), input("Type name: "))

    try:
        excelFile.save(excelPath)
    except PermissionError:
        print("Error: Excel file is currently open.")

    os.system("pause")