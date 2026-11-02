from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home():
    return "Chal chututiya agya chl"


# create user model 

class userModel(BaseModel):
    name: str
    age: int
    status: bool=True

@app.post("/create")
def creataUser(user:userModel):
    return {
        "message": "User create",
        "user":user
    }


# nested response 
class addressModel(BaseModel):
    city:str
    pincode: int
    teh:str
    village:str
class create_user(BaseModel):
    name: str
    age:int
    mobileNo:int
    address:addressModel

@app.post("/create_user")
def create_user(user:create_user):
    return {
        "message": "create user",
            "user":user
            }



# custom response 

# create model
class companyModel(BaseModel):
    company_name: str
    city: str
    pincode: int
    department: str


class employeeModel(BaseModel):
    employee_id: int
    name: str
    age: int
    email: str
    password:str
    company: companyModel


class responseModel(BaseModel):
    name: str
    email: str
    company: companyModel


@app.post("/profile")

def profile(profile: employeeModel):
    public_user = responseModel(
        name= profile.name,
        email=profile.email,
        company=profile.company
    )
    return {
        "message":"User Created",
        "profile":public_user


    }