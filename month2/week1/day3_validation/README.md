# 🔹 День 3 — Валидация данных (Pydantic)

---

## 🧠 Теория

### Что такое Pydantic и зачем он нужен

Pydantic — это библиотека, которая использует аннотации типов Python (type hints) для:

- проверки и валидации входных данных;
- преобразования типов (например, "123" → int(123));
- сериализации и десериализации объектов (в/из JSON);
- автоматического создания документации (в FastAPI);
- обеспечения целостности данных в бизнес-логике.

**Основан на идее: данные должны соответствовать структуре, объявленной в модели.**

## Основные концепции Pydantic

1. BaseModel

Главный строительный блок Pydantic — это класс BaseModel.

```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool = True

user = User(id="1", name="Alice")
print(user)         # id=1 name='Alice' is_active=True
print(user.id)      # 1 (автоматическое приведение типов)
```

- Pydantic проверяет типы при создании экземпляра и конвертирует их, если возможно.
- Если данные не соответствуют схеме — выбрасывается ValidationError.

2. Валидация данных

Модель может проверять и конвертировать типы:

```python
from pydantic import BaseModel, ValidationError

class Product(BaseModel):
    name: str
    price: float

try:
    p = Product(name="Apple", price="12.5")
except ValidationError as e:
    print(e)
else:
    print(p)
```

Pydantic автоматически приведёт "12.5" к float(12.5).

3. Field()

Позволяет указывать метаданные, значения по умолчанию и ограничения:

```python
from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, description="Имя пользователя")
    age: int = Field(..., ge=0, le=120)
```

📘 Параметры:
	•	default / ... — значение по умолчанию / обязательное поле
	•	min_length, max_length — ограничения для строк
	•	ge, le, gt, lt — числовые ограничения
	•	description, example — метаданные для Swagger-документации (FastAPI)

4. Валидаторы (@validator и @field_validator)

Позволяют создавать кастомную логику проверки:

```python
from pydantic import BaseModel, field_validator

class User(BaseModel):
    name: str
    age: int

    @field_validator("age")
    def age_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("Возраст должен быть положительным")
        return v
```

5. Модели в моделях (вложенные структуры)

```python
class Address(BaseModel):
    city: str
    zip: str

class User(BaseModel):
    name: str
    address: Address

u = User(name="Alice", address={"city": "Tbilisi", "zip": "0108"})
print(u.address.city)  # Tbilisi
```

Pydantic автоматически создаёт вложенный объект Address.

6. Сериализация

Преобразование модели обратно в словарь или JSON:

```python
user = User(id=1, name="Alice")
print(user.dict())   # {'id': 1, 'name': 'Alice', 'is_active': True}
print(user.json())   # {"id": 1, "name": "Alice", "is_active": true}
```

7. Immutable модели

Можно запретить изменение значений после создания:

```python
class ConfigExample(BaseModel):
    x: int

    class Config:
        frozen = True

obj = ConfigExample(x=10)
# obj.x = 20  # ❌ TypeError: "ConfigExample" is frozen
```

8. Config / model_config

В Pydantic v2 конфигурация задаётся через **model_config**:

```python
from pydantic import BaseModel, ConfigDict

class User(BaseModel):
    model_config = ConfigDict(extra='ignore', frozen=True)

    name: str
    age: int
```

### Где используется

- FastAPI — для схем запросов/ответов (Request, Response).
- -слой — для DTO (Data Transfer Object) между слоями.
-  и конфигурации — парсинг .env, JSON, YAML.

### Сравнение Pydantic v1 и v2

| Концепт                          | Pydantic v1                                        | Pydantic v2                                                                           | Комментарий                               |
|----------------------------------|----------------------------------------------------|---------------------------------------------------------------------------------------|-------------------------------------------|
| **Импорт**                       | `from pydantic import BaseModel, validator, Field` | `from pydantic import BaseModel, field_validator, model_validator, Field, ConfigDict` | Введены новые декораторы и конфигурации   |
| **Конфигурация модели**          | Через вложенный класс `class Config:`              | Через поле `model_config = ConfigDict(...)`                                           | Более декларативный и современный стиль   |
| **Валидаторы полей**             | `@validator('field')`                              | `@field_validator('field')`                                                           | Новый декоратор, старый — устарел         |
| **Валидаторы модели (root)**     | `@root_validator`                                  | `@model_validator(mode='before'/'after')`                                             | Разделено на этапы до/после валидации     |
| **Тип валидации**                | `@validator(..., pre=True)`                        | `@model_validator(mode='before')`                                                     | Новый параметр `mode` заменяет `pre`      |
| **Параметр Config.extra**        | `class Config: extra = 'ignore'`                   | `model_config = ConfigDict(extra='ignore')`                                           | То же поведение, другой синтаксис         |
| **Иммутабельность (frozen)**     | `class Config: frozen = True`                      | `model_config = ConfigDict(frozen=True)`                                              | Новый способ задания                      |
| **Методы `.dict()` и `.json()`** | Поддерживаются                                     | Поддерживаются, но предпочтительнее `.model_dump()` и `.model_dump_json()`            | Новые методы дают больше контроля         |
| **Создание из ORM**              | `Config.orm_mode = True` + `.from_orm()`           | `model_config = ConfigDict(from_attributes=True)`                                     | Новое имя и подход                        |
| **Ошибки валидации**             | `ValidationError`                                  | `ValidationError` (но структура сообщений изменилась)                                 | Формат стал чище и удобнее                |
| **Валидация коллекций**          | Автоматическая                                     | Всё ещё автоматическая, но оптимизирована                                             | Быстрее и с меньшими накладными расходами |
| **Производительность**           | Медленнее                                          | До **5× быстрее**                                                                     | Переписан на Rust (через `pydantic-core`) |
| **Совместимость**                | Поддерживается до 2024+                            | Рекомендуется для новых проектов                                                      | `Pydantic v1` устаревает                  |

Пример сравнения кода

Pydantic v1

```python
from pydantic import BaseModel, validator

class User(BaseModel):
    name: str
    age: int

    @validator("age")
    def check_age(cls, v):
        if v < 0:
            raise ValueError("Возраст не может быть отрицательным")
        return v

    class Config:
        extra = "ignore"
        frozen = True
```

Pydantic v2

```python
from pydantic import BaseModel, field_validator, ConfigDict

class User(BaseModel):
    model_config = ConfigDict(extra='ignore', frozen=True)

    name: str
    age: int

    @field_validator("age")
    @classmethod
    def check_age(cls, v):
        if v < 0:
            raise ValueError("Возраст не может быть отрицательным")
        return v
```

| 🚀 Возможность                                          | 📝 Описание                                             |
|---------------------------------------------------------|---------------------------------------------------------|
| **pydantic-core**                                       | Новое ядро на **Rust**, ускоряющее парсинг и валидацию  |
| **field_validator / model_validator**                   | Более точный контроль за этапами валидации              |
| **model_dump / model_validate**                         | Новые универсальные методы для сериализации и валидации |
| **computed_field**                                      | Возможность создавать вычисляемые свойства              |
| **Улучшенная поддержка dataclasses**                    | Полная интеграция с `@dataclass`                        |
| **Валидация на уровне модели (`mode='before'/'after')** | Гибкость в зависимости от логики валидации              |

### Что такое BaseSettings

BaseSettings — это специальный класс Pydantic, предназначенный для управления настройками и конфигурацией приложения.
Он расширяет BaseModel, добавляя автоматическую загрузку данных из окружения (environment variables).

То есть, вы можете объявить класс с параметрами приложения — и Pydantic автоматически заполнит его из:
- .env файла,
- переменных окружения (например, export DB_URL=...),
- значений по умолчанию в коде.

Пример (Pydantic v2)

```python
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    app_name: str = "MyApp"
    debug: bool = False
    database_url: str

settings = Settings()
print(settings)
```

.env:
```bash
DEBUG=True
DATABASE_URL=postgresql://user:pass@localhost:5432/mydb
```

Результат

```commandline
app_name='MyApp' debug=True database_url='postgresql://user:pass@localhost:5432/mydb'
```

| Возможность                                  | Описание                                                 |
|----------------------------------------------|----------------------------------------------------------|
| **Автоматическая загрузка окружения**        | Читает значения из `.env` и `os.environ`                 |
| **Конфигурация через `SettingsConfigDict`**  | Заменяет старый класс `Config`                           |
| **Поддержка `.env` файла**                   | Используются параметры `env_file` и `env_file_encoding`  |
| **Кастомные имена переменных**               | Настраиваются через параметр `alias`                     |
| **Типизация и валидация**                    | Проверяет корректность типов, как `BaseModel`            |
| **Совместимость с FastAPI**                  | Можно внедрять через `Depends`                           |

Пример с alias и валидацией

```python
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    db_url: str = Field(..., alias="DATABASE_URL")
    api_key: str = Field(..., alias="API_KEY")
    debug: bool = False

settings = Settings()
print(settings.db_url)
```

.env
```bash
DATABASE_URL=sqlite:///./test.db
API_KEY=12345
```

### Отличия между Pydantic v1 и v2

| Концепт              | v1                                  | v2                                           | Комментарий                 |
|----------------------|-------------------------------------|----------------------------------------------|-----------------------------|
| **Импорт**           | `from pydantic import BaseSettings` | `from pydantic_settings import BaseSettings` | Вынесено в отдельный пакет  |
| **Конфигурация**     | `class Config:`                     | `SettingsConfigDict`                         | Новый способ настройки      |
| **Параметры `.env`** | `env_file`, `env_file_encoding`     | Те же параметры через `SettingsConfigDict`   | Сохранена совместимость     |
| **Поведение**        | Поддерживает `.env` и `os.environ`  | То же, но быстрее                            | Улучшена производительность |

### Использование с FastAPI

```python
from fastapi import FastAPI, Depends
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FastAPI App"
    admin_email: str
    debug: bool = False

settings = Settings()

app = FastAPI()

@app.get("/info")
def info(cfg: Settings = Depends(lambda: settings)):
    return {"app_name": cfg.app_name, "debug": cfg.debug}
```


## Структура

