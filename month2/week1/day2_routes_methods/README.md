# 🔹 День 2 — Маршруты и методы (GET, POST, PUT, DELETE)

---

## 🧠 Теория

- @app.get(), @app.post(), @app.put(), @app.delete()

### 1️⃣ Query-параметры (Query)

Суть
	•	Значения передаются через строку запроса (?key=value).
	•	Используется для фильтров, поиска, пагинации.

```python
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
def read_items(q: str = Query(None, min_length=3)):
    return {"q": q}
```

Пример

```pseudocode
GET /items/?q=apple
```

### 2️⃣ Path-параметры (Path)

- body — данные в теле запроса (JSON, form, file и т.д.).

Суть
	•	Значения передаются в самом пути URL (/items/{item_id}).
	•	Используется для уникальной идентификации ресурса.

```python
from fastapi import Path

@app.get("/items/{item_id}")
def read_item(item_id: int = Path(..., ge=1)):
    return {"item_id": item_id}
```

```pseudocode
GET /items/42
```

3️⃣ Body-параметры (Body)

Суть
	•	Значения передаются в теле запроса, чаще всего в формате JSON.
	•	Используется для создания или обновления ресурсов.

```python
from fastapi import Body
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float

@app.post("/items/")
def create_item(item: Item = Body(...)):
    return item
```

Пример запроса (JSON)
```commandline
POST /items/
{
  "name": "Apple",
  "price": 1.5
}
```

### Роутеры (APIRouter) для организации кода.

- post, put, delete, patch — определяют CRUD-эндпоинты.
- lude_router — делает проект модульным и читаемым.
- _api_route — полезен при динамической регистрации маршрутов.
- event — для инициализации и освобождения ресурсов.
- socket — при работе с реальным временем (чат, уведомления).

## Ключевые методы APIRouter

| Метод            | Назначение                                           | Пример                            |
|------------------|------------------------------------------------------|-----------------------------------|
| get()            | Регистрирует обработчик HTTP GET-запроса.            | @router.get("/users")             |
| post()           | Регистрирует обработчик POST-запроса.                | @router.post("/users")            |
| put()            | Регистрирует обработчик PUT-запроса.                 | @router.put("/users/{id}"         | 
| delete()         | Регистрирует обработчик DELETE-запроса.              | @router.delete("/users/{id}"      |  
| patch()          | Регистрирует обработчик PATCH-запроса.               | @router.patch("/users/{id}"       |
| include_router() | Подключает другой APIRouter к текущему.              | router.include_router(auth_router |
|                  | Используется для модульной структуры.                | , prefix="/auth"                  |
| add_api_route()  | Программно добавляет маршрут (без декоратора).       | router.add_api_route("/info"      |
|                  |                                                      | , endpoint=get_info)              |
| on_event()       | Добавляет обработчик событий приложения              | @router.on_event("startup")       |
|                  | (например, при старте).                              |                                   |
| url_path_for()   | Возвращает путь по имени маршрута                    | router.url_path_for               |
|                  | (удобно при динамической генерации ссылок).          | ("read_user", user_id=1)          |
| websocket()      | Создаёт WebSocket-маршрут (для двусторонней связи).  | @router.websocket("/ws")          |

## Структура

```commandline
day2_routes_methods/
├── main.py          # Точка входа
├── router.py        # Все маршруты
├── models.py        # Pydantic-модели
├── data.py          # Хранилище (in-memory list)
└── test_products.py # Тесты CRUD

```