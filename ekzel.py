import os
import openpyxl

absolutePath=os.path.dirname(os.path.abspath(__file__)) # Find actual directory
excelPath=os.path.join(absolutePath, "queso.xlsx") # Find directory's excel

excelFile = ""
excelSheet = ""

def open_excel():
    global excelFile, excelPath, excelSheet

    try:
        excelFile=openpyxl.load_workbook(excelPath)
        excelSheet=excelFile["promedio"]
    except:
        print("Error: File doesn't exist or is already open.")

    return

def write_excel():
    open_excel()






















#excelpath es ela rchivo
#excelsheet es la hoja
#excelfile es el cos carpeta
#eso no impporta


def write_cell(row:float, column:float, data:str):
    global excelPath, excelSheet, excelFile

    open_excel()#abre el archivo
    excelSheet.cell(row, column, data)
    #celda segun row columna y el dato, ese es el orden pues
    excelFile.save(excelPath)

