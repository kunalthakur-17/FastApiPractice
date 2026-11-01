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

# mulltipal api

@app.get("/about")
def about():
    return {
        "message": "This is about API",
        "company": "Tech Solutions",
        "founded": 2020,
        "location": "India",
        "services": [
            "Web Development",
            "API Development",
            "Database Management"
        ],
        "is_active": True
    }


@app.get("/profile")
def profile():
    return {
        "message": "This is profile API",
        "user": {
            "id": 101,
            "name": "Rahul Sharma",
            "age": 25,
            "email": "rahul@example.com",
            "city": "Delhi",
            "is_active": True
        },
        "skills": ["Python", "FastAPI", "JavaScript"],
        "experience": 2,
        "is_available": False
    }


# Path Parameters

@app.get("/user/{user_id}")
def user(user_id: int):
    return {
        "message": "User details fetched successfully",
        "user": {
            "id": user_id,
            "name": "Rahul Sharma",
            "age": 25,
            "email": "rahul@example.com",
            "city": "Delhi",
            "skills": ["Python", "FastAPI", "React JS"],
            "is_active": True
        }
    }