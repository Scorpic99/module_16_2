from typing import Annotated

import uvicorn
from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/")
async def main_page():
    return "Главная страница"

@app.get("/user/admin")
async def admin_panel():
    return "Вы вошли как администратор"

@app.get("/user")
async def info_panel(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", exemple="UrbanUser")]
                     , age: Annotated[int, Path(ge=18, le=120, description="Enter age", exemple="24")]):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"

@app.get("/user/{user_id}")
async def user_panel(user_id: int = Path(ge=1, le=100, description="Enter User ID", exemple="10",)):
    return f"Вы вошли как пользователь № {user_id}"

if __name__ == "__main__":
    uvicorn.run(app , host="127.0.0.1", port=8000)