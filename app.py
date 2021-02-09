import api
from models.student import Student

def born_in(age : int):
    return 2020 - age

student = Student(**api.get_student())
print(f'{student.name} born in {born_in(student.age)}')
