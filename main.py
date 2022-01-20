from typing import List
from uuid import uuid4, UUID
from fastapi import FastAPI, HTTPException
from models import Gender, Role, User ; 

app = FastAPI()

db: List[User] = [
    User(
        id= UUID("46acbfb8-4fb8-46ba-bdcb-27e361d0617e"), 
        first_name= "M", 
        last_name= "J", 
        gender= Gender.male,  
        roles= [Role.student]
    ),
    User(
        id= UUID("1d893484-a30d-498f-a610-b5ab5565f84c"), 
        first_name= "Nina", 
        last_name= "J", 
        gender= Gender.female,  
        roles= [Role.student, Role.admin]
    )
]

@app.get("/")
def root(): 
    return {"Hello": "World"}

@app.get("/api/v1/users")
async def fetch_users():
    return db


@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user) # do not restart the server and the db get request as well returns the appended objects
    return db ; 


@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db: 
        if user.id== user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404, 
        detail=f"user with id: {user_id} does not exist"
    )
    





# http://localhost:8000/
# http://localhost:8000/docs   -> swagger 
# http://localhost:8000/redoc  -> documentation 
# middle_name= Optional[str]