from fastapi import FastAPI
from fastapi import Query

# Создание экземпляра приложения FastAPI
app = FastAPI()

# Определение маршрута для главной страницы
@app.get("/")
async def read_root():
    return {"message": "Главная страница"}

# Определение маршрута для страницы администратора
@app.get("/user/admin")
async def read_admin():
    return {"message": "Вы вошли как администратор"}

# Определение маршрута для страницы пользователя с параметром в пути
@app.get("/user/{user_id}")
async def read_user(user_id: int):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

# Определение маршрута для страницы пользователя с данными в адресной строке
@app.get("/user")
async def read_user_info(username: str = Query(...), age: int = Query(...)):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}

