from fastapi import FastAPI

app = FastAPI()


@app.get("/users/me")
def read_user_me():
    return {"user_id": "current user"}


@app.get("/users/{user_id}")
def read_params(user_id: str):
    return {"user_id": user_id}