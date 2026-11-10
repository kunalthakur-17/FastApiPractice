from fastapi import FastAPI
from MokeData import Products
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Server is working"}

@app.get("/products")
def products():
    return {
        "Message": "All data",
        "length":len(Products),
        "data":Products
    }
@app.get("/product/{id}")
def product(id:int):
    for product in Products:
        if product["id"]==id:
            return product
    return {
        "message" :"Id not match"
    }