import openpyxl
from extras import students
from extras import arreglos
wb = ""
ws = ""

def open_excel():
    try:
        global wb, ws
        wb=openpyxl.load_workbook("C:/Users/Justie/Desktop/Tareas/Programacion para Ingenieros/Segundo parcial/Python-Grading-System")
        ws=wb["promedio"]
        print("Excel file successfully opened.")
    except:
        print("Error: Excel file may not exist or be opened.")
    
    return
    
def write_excel():
    countrow=ws.max_row
    countcolumn=ws.max_column
    z=0
    for i in range(2, countrow+1):
        ws.cell(row=i, column=1, value=arreglou[z] )
        z+=1
        wb.save("C:/Users/Justie/Desktop/Tareas/Programacion para Ingenieros/Segundo parcial/Python-Grading-Syste/queso.xlsx")
write_excel()