# 🔹 День 4 — Ответы и коды состояния (HTTPException, status_code)

---

## 🧠 Теория

### FastAPI позволяет управлять HTTP-ответами через:

- status_code в декораторах (@app.get(..., status_code=201))
- HTTPException для ошибок (raise HTTPException(status_code=404, detail="Not found"))

### Стандартные HTTP-коды:

- 200 OK — успешный запрос
- 201 Created — создан ресурс
- 204 No Content — удаление прошло успешно, тело пустое
- 400 Bad Request — неверные данные запроса
- 404 Not Found — ресурс не найден
- 422 Unprocessable Entity — Pydantic не прошёл валидацию

### Что сделан
| Требование                                                       | Статус      | Где реализовано                                                     |
|------------------------------------------------------------------|-------------|---------------------------------------------------------------------|
| 201 Created при создании                                         | выполнено   | @items_router.post("/", status_code=status.HTTP_201_CREATED)        |
| 404 Not Found при отсутствии элемента                            | выполнено   | во всех методах через HTTPException(status_code=404)                |
| 400 Bad Request при конфликте / ошибке данных                    | выполнено   | except ItemAlreadyExistsError и except ItemNotChangedError          |
| 409 Conflict при дублировании имени                              | выполнено   | except ItemAlreadyExistsError                                       |
| 204 No Content при удалении                                      | выполнено   | @items_router.delete(..., status_code=status.HTTP_204_NO_CONTENT)   |
| Возврат стандартизированных ответов                              | выполнено   | InfoResponse, ItemListResponse                                      |
| Использование responses={...} в аннотациях                       | выполнено   | для всех маршрутов                                                  |
| Подробные docstring для Swagger                                  | выполнено   | каждый endpoint имеет summary, description и example                |


- Interface слой отвечает за валидацию, ответы и статус-коды.
- Application слой — бизнес-логика (items_service).
- Domain слой — содержит исключения (ItemNotFoundError, ItemAlreadyExistsError, ItemNotChangedError).
- Infrastructure слой — in-memory репозиторий.

Дополнительно

-	Пагинация (PaginationMeta + ItemListResponse)
-	Унифицированная InfoResponse (мета-обёртка для API)
-	Поддержка Query параметров (page, per_page)
-	Примеры (example= в Path)
-	Документация в стиле OpenAPI (через summary, description, responses)