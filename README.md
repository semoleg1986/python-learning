# 🐍 Python Learning Roadmap

---

## 📅 Roadmap по месяцам

### Месяц 1 — База Python
- [x] Неделя 1: Базовые структуры и строки  
  - [x] Day 1: Numbers (`is_even`, `digit_sum`, `factorial`)  
  - [x] Day 2: Strings (`reverse_string`, `is_palindrome`, `count_vowels`)  
  - [x] Day 3: Lists, Docstring (`unique`, `flatten`, `find_max_min`)  
  - [x] Day 4: Tuples & Sets (`common_elements`, `most_frequent`, `remove_duplicates`)
  - [x] Day 5: Dictionaries (`char_frequency`, `merge_dicts`, `invert_dict`)
  - [x] Day 6: Combined tasks (`count_of_words`, `freq_chars`, `remove_duplicates_words`, `reverse_words`, `top3_words`)
  - [x] Day 7: Mini-project → **Word Analyzer**
- [x] Неделя 2: Функции, модули и ООП
  - [x] Day 1: Functions & Arguments (`sum_all`, `print_info`, `calc_avg`)
  - [x] Day 2: Lambda, Map, Filter, Reduce (`squares`, `filter_even`, `product`)
  - [x] Day 3: Classes & Objects (`Person`, `Circle`, `Book`)
  - [x] Day 4: Inheritance & Polymorphism (`Animal`, `Dog`, `Cat`, `Account`, `SavingsAccount`)
  - [x] Day 5: Modules & Imports (`random_sqrt`, `current_date`, `from_math_utils`)
  - [x] Day 6: Combined Tasks (`Stats`, `sort_and_filter`, `count_letters_in_file`)
  - [x] Day 7: Mini-project: **CLI Calculator** 
- [x] Неделя 3: Исключения, файлы и стандартные модули
  - [x] Day 1: Exception Handling (`divide`, `safe_int`, `access_list_element`)
  - [x] Day 2: Custom Exceptions (`NegativeValueError`, `InvalidAgeError`, `check_age`)
  - [x] Day 3: File Operations (`read_file`, `write_file`, `append_line`)
  - [x] Day 4: Pathlib & File Paths (`list_files`, `create_folder`, `file_info`)
  - [x] Day 5: Standard Modules (`current_time`, `combine_lists`, `multiply_all`)
  - [x] Day 6: Combined Tasks (`read_json`, `count_lines_with_word`, `safe_write`)
  - [x] Day 7: Mini-project: **Log Analyzer CLI**
- [x] Неделя 4: Git, практика и мини-проект
  - [x] Day 1: Git Basics (`git init`, `git add`, `git commit`, `git log`)
  - [x] Day 2: Branches & Remote (`git branch`, `git merge`, `git push`, `git pull`)
  - [x] Day 3: Pull Requests & Code Review (`feature/day3`, `PR`, `merge`)
  - [x] Day 4: .gitignore & SSH (`.gitignore`, `exclude`, `SSH keys`)
  - [x] Day 5: Git Flow & Tags (`git flow`, `git revert`, `git reset`, `git tag`)
  - [x] Day 6: Combined Git Tasks (`develop`, `feature`, `.pre-commit`)
  - [x] Day 7: Mini-project: **CLI Password Manager** (`add_password`, `remove_password`, `find_password`)
---

### Месяц 2 — Введение в Backend (FastAPI)
- [ ] Неделя 1: Основы FastAPI и REST 
  - [x] Day 1: Введение в FastAPI (`Hello, FastAPI!`)  
  - [x] Day 2: Маршруты и методы (`/tasks`, CRUD)  
  - [x] Day 3: Валидация данных (Pydantic, `TaskCreate`, `TaskUpdate`)  
  - [x] Day 4: Ответы и коды состояния (`HTTPException`, `status_code`)  
  - [ ] Day 5: Организация кода (`routers/`, `models/`, `schemas/`)  
  - [ ] Day 6: Комбинированные задачи (фильтрация, поиск)  
  - [ ] Day 7: Mini-project: **ToDo API (in-memory)**
- [ ] Неделя 2: PostgreSQL и SQLAlchemy
  - [ ] Day 1: Подключение PostgreSQL (`psycopg2`, DATABASE_URL)  
  - [ ] Day 2: SQLAlchemy ORM (`Task`, `Base`, `SessionLocal`)  
  - [ ] Day 3: CRUD через ORM  
  - [ ] Day 4: Dependency Injection (`Depends(get_db)`)  
  - [ ] Day 5: Конфигурация (.env, BaseSettings)  
  - [ ] Day 6: Комбинированные задачи (пагинация, сортировка)  
  - [ ] Day 7: Mini-project: **ToDo API + Database**
- [ ] Неделя 3: Alembic и аутентификация (JWT)
  - [ ] Day 1: Миграции Alembic (`init`, `revision`, `upgrade`)  
  - [ ] Day 2: Модель пользователя (`User`)  
  - [ ] Day 3: Хэширование паролей (`passlib[bcrypt]`)  
  - [ ] Day 4: JWT токены (`python-jose`, OAuth2PasswordBearer)  
  - [ ] Day 5: Middleware и защита маршрутов (`Depends(current_user)`)  
  - [ ] Day 6: Комбинированные задачи (Users + Tasks)  
  - [ ] Day 7: Mini-project: **ToDo API с JWT-аутентификацией**
- [ ] Неделя 4: Валидация, тестирование и документация
  - [x] Day 1: Расширенная валидация (`EmailStr`, `constr`, `validator`)  
  - [ ] Day 2: Тестирование API (`pytest`, `httpx.AsyncClient`)  
  - [ ] Day 3: Документация Swagger / ReDoc (`/docs`, `/redoc`)  
  - [ ] Day 4: Конфигурация окружения (`.env`, `.env.example`)  
  - [ ] Day 5: Подготовка к деплою (проверка эндпоинтов, статусов, тестов)  
  - [ ] Day 6: Комбинированные задачи (тесты авторизации)  
  - [ ] Day 7: Mini-project: **ToDo API v2 (JWT + Tests + Docs)**

---

### Месяц 3 — Бэкенд и базы данных
- [ ] Flask / FastAPI  
- [ ] SQL и SQLAlchemy  
- [ ] Alembic (миграции)  
- [ ] Docker и docker-compose  

---

### Месяц 4 — Тестирование и DevOps
- [ ] Pytest (юнит, интеграционные тесты)  
- [ ] CI/CD (GitHub Actions)  
- [ ] Логирование и мониторинг  

---

### Месяц 5 — Проекты для портфолио
- [ ] REST API для блога (Flask/FastAPI + PostgreSQL)  
- [ ] Мини-маркетплейс (DDD + микросервисы)  
- [ ] Telegram-бот (aiogram + Docker)  

---

## 📂 Структура репозитория
```commandline
python-learning/
│
├── Makefile                        # Команды для запуска тестов, линтинга, миграций и др.
├── README.md                       # Описание проекта
├── requirements.in                 # Исходный список зависимостей
├── requirements.txt                # Сгенерированные зависимости
├── .gitignore                      # Список игнорируемых файлов
├── pytest.ini                      # Конфигурация pytest
├── pyproject.toml                  # Настройки black, isort и других инструментов
├── mypy.ini                        # Настройки mypy
├── .flake8                         # Настройки flake8
├── .pre-commit-config.yaml         # Конфигурация pre-commit хуков
│
├── week1/                          # Неделя 1 — Numbers, Strings, Lists…
│   ├── init.py
│   ├── day1_numbers.py
│   ├── day2_strings.py
│   ├── day3_lists.py
│   ├── day4_tuples_and_sets.py
│   ├── day5_dict.py
│   └── day6_combine.py
│
├── tests/                          # Тесты
│   ├── init.py
│   ├── week1/
│   │   ├── init.py
│   │   ├── test_day1_numbers.py
│   │   ├── test_day2_strings.py
│   │   ├── test_day3_lists.py
│   │   ├── test_day4_tuples_and_sets.py
│   │   ├── test_day5_dict.py
│   │   └── test_day6_combine.py
│   │
│   └── week2/
│       ├── day1_functions.py
│       ├── day2_lambda.py
│       ├── day3_classes.py
│       ├── day4_inheritance.py
│       ├── day5_modules.py
│       ├── day6_combine.py
│       ├── math_utils.py
│       └── test.txt
│
├── projects/                       # Мини-проекты
│   ├── init.py
│   ├── cli_calculator/
│   │   ├── Makefile
│   │   ├── README.md
│   │   ├── __init__.py
│   │   ├── calculator.py          # Логика вычислений
│   │   ├── cli.py                 # CLI-интерфейс (App)
│   │   ├── main.py                # Точка входа
│   │   ├── utils/
│   │   │   ├── __init__.py
│   │   │   └── logger.py          # Настройка логирования
│   │   └── tests/
│   │       ├── __init__.py
│   │       └── test_cli_calculator.py  # Юнит-тесты
│   └── word_analyzer/              # CLI Word Analyzer
│       ├── init.py
│       ├── analyzer.py             # Анализатор текста
│       ├── cli.py                  # CLI-приложение
│       ├── main.py                 # Запускает приложение
│       ├── README.md
│       ├── Makefile
│       ├── tests                   # Тесты
│       │   ├── init.py
│       │   └── test_analyzer.py
│       │
│       └── utils/                  # Логгирование
│           ├── init.py
│           └── logger.py
│
└── docs/                           # Документация
    └── python_r.xlsx
```