from fastapi import FastAPI
from app.grpc_client import get_user_by_id

app = FastAPI()

@app.get("/users/{user_id}")
def read_user(user_id: int):
    user = get_user_by_id(user_id)
    return {
        "id": user.id,
        "name": user.name,
        "email": user.email
    }
