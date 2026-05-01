from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# temporary storage
users = []

# data model


class User(BaseModel):
    name: str
    email: str
    password: str


@app.get("/")
def home():
    return {"message": "IntraMail backend running"}


# SIGNUP
@app.post("/signup")
def signup(user: User):
    users.append(user)
    return {"message": "User registered successfully"}


# LOGIN
@app.post("/login")
def login(user: User):
    for u in users:
        if u.email == user.email and u.password == user.password:
            return {"status": "login success"}
    return {"status": "invalid credentials"}
