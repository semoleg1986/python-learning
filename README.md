# 🐍 Python Learning Roadmap

---

## 📅 Roadmap по месяцам

### Месяц 1 — База Python
- [ ] Неделя 1: Базовые структуры и строки  
  - [x] Day 1: Numbers (`is_even`, `digit_sum`, `factorial`)  
  - [x] Day 2: Strings (`reverse_string`, `is_palindrome`, `count_vowels`)  
  - [x] Day 3: Lists, Docstring (`unique`, `flatten`, `find_max_min`)  
  - [x] Day 4: Tuples & Sets  
  - [ ] Day 5: Dictionaries  
  - [ ] Day 6: Combined tasks  
  - [ ] Day 7: Mini-project → **Word Analyzer**
- [ ] Неделя 2: Управление потоком (if/for/while), функции  
- [ ] Неделя 3: ООП (классы, наследование, инкапсуляция)  
- [ ] Неделя 4: Модули, работа с файлами, pytest

---

### Месяц 2 — Продвинутый Python
- [ ] Исключения и обработка ошибок  
- [ ] Итераторы, генераторы, декораторы  
- [ ] Модули `itertools`, `functools`, `collections`  
- [ ] Асинхронность: `asyncio`, `aiohttp`

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
│   └── day3_lists.py
│
├── tests/                          # Тесты
│   ├── init.py
│   └──  week1/
│       ├── init.py
│       ├── test_day1_numbers.py
│       ├── test_day2_strings.py
│       ├── test_day3_lists.py
│       └── test_day4_tuples_and_sets.py
│
├── projects/                       # Мини-проекты
│
└── docs/                           # Документация
    └── python_r.xlsx
```