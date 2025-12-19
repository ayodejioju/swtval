from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "name": "Ayodeji"}

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# -----------------------------
# Data Model
# -----------------------------
class User(BaseModel):
    name: str
    email: str

# Fake in-memory database
users = {}

# -----------------------------
# CREATE (POST)
# -----------------------------
@app.post("/users")
def create_user(user: User):
    user_id = len(users) + 1
    users[user_id] = user
    return {"id": user_id, "user": user}

# -----------------------------
# READ (GET)
# -----------------------------
@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": user_id, "user": users[user_id]}

# -----------------------------
# UPDATE (PUT)
# -----------------------------
@app.put("/users/{user_id}")
def update_user(user_id: int, updated_user: User):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users[user_id] = updated_user
    return {"id": user_id, "user": updated_user}

# -----------------------------
# DELETE (DELETE)
# -----------------------------
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    del users[user_id]
    return {"message": "User deleted successfully"}