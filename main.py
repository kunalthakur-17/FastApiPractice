from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Welcome to FastAPI",
        "status": "success",
        "user": {
            "id": 101,
            "name": "Kunal",
            "age": 27,
            "email": "kunal@example.com",
            "is_active": True
        },
        "skills": ["Python", "FastAPI", "React JS", "SQL"],
        "address": {
            "city": "Dharamshala",
            "state": "Himachal Pradesh",
            "country": "India"
        },
        "projects": [
            {
                "id": 1,
                "name": "Student Management System",
                "completed": True
            },
            {
                "id": 2,
                "name": "Employee Management System",
                "completed": False
            }
        ]
    }