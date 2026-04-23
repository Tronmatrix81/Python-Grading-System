students = {394569: "Eric Gallo Gardea", 
            394468: "Josue Caleb Escobedo Herrera", 
            394350: "Justie Ariel Loya Martinez"}

def FindStudent(num: int)-> str:
    return students.get(num, "Student not found!")