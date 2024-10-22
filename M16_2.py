from fastapi import FastAPI, Path
from typing import Annotated

# Создание экземпляра приложения FastAPI
app = FastAPI()


# Определение маршрута для главной страницы
@app.get("/")
async def read_root() -> dict:
    return {"message": "Главная страница"}


# Определение маршрута для страницы администратора
@app.get("/user/admin")
async def read_admin() -> dict:
    return {"message": "Вы вошли как администратор"}


# Определение маршрута для страницы пользователя с валидацией параметра в пути
@app.get("/user/{user_id}")
async def read_user(
        user_id: Annotated[int, Path(
            ge=1, le=100, description="Ввежите свой id", example=1
        )]
):
    return {"message": f"Вы вошли как пользователь № {user_id}"}


# Определение маршрута для страницы пользователя с валидацией параметров в пути
@app.get("/user/{username}/{age}")
async def read_user_info(
        username: Annotated[str, Path(
            min_length=5, max_length=20, description="Введите имя", example="Dave Mustaine "
        )],
        age: Annotated[int, Path(
            ge=18, le=120, description="Введите возраст", example=24
        )]
) -> dict:
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
