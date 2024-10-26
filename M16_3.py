from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

# Инициализация словаря пользователей
users = {'1': 'Имя: Example, возраст: 18'}


# GET запрос для получения всех пользователей
@app.get("/users")
async def get_users() -> dict:
    return users


# POST запрос для добавления нового пользователя
@app.post("/user/{username}/{age}")
async def create_user(
        username: Annotated[str, Path(
            min_length=5, max_length=20, description="Введите имя", example="Dave Mustaine "
        )],
        age: Annotated[int, Path(
            ge=18, le=120, description="Введите возраст", example=24
        )]
) -> str:
    # Находим максимальный ключ в словаре
    current_index = str(int(max(users, key=int)) + 1)
    users[current_index] = f"Имя: {username}, возраст: {age}"
    return f"User  {current_index} is registered"


# PUT запрос для обновления информации о пользователе
@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
        user_id: Annotated[str, Path(min_length=1
        )],
        username: Annotated[str, Path(
            min_length=5, max_length=20, description="Введите имя", example="Dave Mustaine "
        )],
        age:Annotated[int, Path(
            ge=18, le=120, description="Введите возраст", example=24
        )]
) -> str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User  {user_id} has been updated"


# DELETE запрос для удаления пользователя
@app.delete("/user/{user_id}")
async def delete_user(user_id:Annotated[str, Path(min_length=1)]):
    users.pop(user_id)
    return f"User  {user_id} has been deleted"


