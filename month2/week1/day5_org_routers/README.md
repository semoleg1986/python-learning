# 🔹 День 5 — Организация кода (Routers))

---

## 🧠 Теория

	•	Разделяй проект на модули по назначению (items, users, tasks и т.д.).
	•	Используй APIRouter для каждого модуля.
	•	Подключай роутеры через include_router() в main.py.
	•	Выноси модели, схемы и бизнес-логику в отдельные слои:
	•	domain/ — сущности (Entity Models)
	•	application/ — команды и сервисы
	•	interface/ — роутеры и схемы
	•	infrastructure/ — хранилища (репозитории)

## ⚙️ Практика

✅ Задачи

1.	Создай два роутера:
   - items_router — CRUD для товаров.
   - users_router — CRUD для пользователей.
2. Подключи оба роутера в interface/api/v1/router.py.
3. Импортируй общий роутер в main.py через include_router.
4. Вынеси модели и схемы в отдельные файлы:
- domain/entities/ → бизнес-модели (ItemModel, UserModel)
- interface/api/v1/items/ → request.py, response.py, router.py
- interface/api/v1/users/ → request.py, response.py, router.py

### Что сделано

✓ Модульная архитектура

✓ Команды (create/update)

✓ Clean + DDD + services + domain

✓ Репозитории отдельно

✓ Тесты на сервисы, репы и API

✓ versioning API (v1/)

## Структура
```commandline
├── main.py
├── application/
│   ├── services/
│   │   ├── item_service.py
│   │   └── user_service.py
│   └── commands/
│       ├── item/
│       │   ├── create_item.py
│       │   └── update_item.py
│       └── user/
│           ├── create_user.py
│           └── update_user.py
├── domain/
│   └── entities/
│       ├── item_model.py
│       └── user_model.py
├── infrastructure/
│   └── repositories/
│       ├── item_memory.py
│       └── user_memory.py
└── interface/
    └── api/
        ├── schemas/
        │   ├── meta.py
        │   └── paginated_response.py
        └── v1/
            ├── router.py
            ├── items/
            │   ├── request.py
            │   ├── response.py
            │   └── router.py
            └── users/
                ├── request.py
                ├── response.py
                └── router.py
```
