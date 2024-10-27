from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel

app = FastAPI()

# Создание пустого списка
users = []


# Создание класса (модели)
class User(BaseModel):
    id: int
    username: str
    age: int


# GET запрос для получения всех пользователей
@app.get("/users")
async def get_users() -> List[User]:
    return users


# POST запрос для добавления нового пользователя
@app.post("/user/{username}/{age}")
async def create_user(username: str, age: int) -> str:
    user_id = len(users) + 1  # Генерация нового ID
    user = User(id=user_id, username=username, age=age)
    users.append(user)
    return f"User  {user_id} is registered"


# PUT запрос для обновления информации о пользователе
@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, username: str, age: int) -> str:
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return f"User  {user_id} is updated"
    raise HTTPException(status_code=404, detail="User  was not found")


# DELETE запрос для удаления пользователя
@app.delete("/user/{user_id}")
async def delete_user(user_id: int) -> str:
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return f"User  {user_id} is deleted"
    raise HTTPException(status_code=404, detail="User  was not found")




