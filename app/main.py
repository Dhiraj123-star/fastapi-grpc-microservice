from fastapi import FastAPI, HTTPException
from app.grpc_client import get_user_by_id, add_fake_user

app = FastAPI()

@app.get("/users/{user_id}")
def read_user(user_id: int):
    try:
        user = get_user_by_id(user_id)
        return {
            "id": user.id,
            "name": user.name,
            "email": user.email
        }
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.post("/users/add")
def create_fake_user():
    user = add_fake_user()
    return {
        "id": user.id,
        "name": user.name,
        "email": user.email
    }
