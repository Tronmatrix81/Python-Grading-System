from team import students

def FindStudent(num: int)-> str:
    return students.get(num, "Student not found!")