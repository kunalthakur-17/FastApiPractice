from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

StudentsList=[]

class StudentModel(BaseModel):
    id: int
    name: str
    age: int
    course: str
    status: bool = True

@app.post("/students")
def create_student(students : StudentModel):
    StudentsList.append(students)
    return {
        "message":"student Created",
        "data":students
    }

# get all student
@app.get("/students")
def get_students():
    if len(StudentsList)<1:
        return "Now student Found here"
    else:
        return {
            "message":"This is all student",
            "Total of students": len(StudentsList),
            "data":StudentsList 
                }

# get student by id

@app.get("/student/{id}")
def get_student(id: int):
    for student in StudentsList:
        if student.id == id:
            return student
    else:
        return "Student id is not found"

# Update api 

@app.put("/student/{id}")
def update_student(id: int, updateModel: StudentModel):
    for index, student in enumerate(StudentsList):
        if student.id == id:
            StudentsList[index] = updateModel
            return {
                "message": "Data Updated Successfully",
                "data": updateModel
            }

    return {"error": "Student not found"}


# Delete api 

@app.delete("/student/{id}")
def delete_Student(id:int):
    for index, student in enumerate(StudentsList):
        if student.id==id:
            StudentsList.pop(index)
            return {"message":"Student Deleted"}
    return {"error": "Student not found"}