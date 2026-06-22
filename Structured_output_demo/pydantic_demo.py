from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = 'pratik'
    age: Optional[int]  = None
    cgpa: float = Field(gt=0, lt=10, default=6)
    # email: EmailStr

new_student = {'age': '32', 'cgpa': 4}
#email validation is also available in pydantic
#'email': 'abc@gmail.com'

student = Student(**new_student)

#pydantic also converts into dictionary and JSON formats
student_dict = dict(student)
student_json = student.model_dump_json()
print(student_dict['cgpa'])