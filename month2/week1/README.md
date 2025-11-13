# Python Learning Roadmap — Month 2, Week 1

---

## 📅 Прогресс

### Week 1 — FastAPI & REST
- [x] Day 1 — Введение в FastAPI (`first_app`, `run_server`)
- [x] Day 2 — Маршруты и методы (`get_items`, `post_item`, `put_item`)
- [x] Day 3 — Валидация данных (Pydantic) (`ItemModel`, `UserModel`, `validate_input`)
- [x] Day 4 — Ответы и коды состояния (`JSONResponse`, `status_code`, `custom_response`)
- [ ] Day 5 — Организация кода (Routers) (`users_router`, `tasks_router`, `include_router`)
- [ ] Day 6 — Combined Tasks (`CRUD_operations`, `query_params`, `path_params`)
- [ ] Day 7 — Mini-project → **ToDo API (in-memory)**

---

## 📂 Projects
- `todo_api/` — Мини-проект CRUD API для задач (Week 1, Day 7)

---

## 🚀 Запуск
```bash
# Установить зависимости
pip install fastapi uvicorn pydantic

# Запуск примеров по дням
python week1/day1_fastapi_intro.py
python week1/day2_routes.py
python week1/day3_pydantic.py
python week1/day4_responses.py
python week1/day5_routers.py
python week1/day6_combined_tasks.py

# Запуск мини-проекта ToDo API
uvicorn projects/todo_api.main:app --reload