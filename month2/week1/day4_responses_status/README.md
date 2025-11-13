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
