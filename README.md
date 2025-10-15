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
- [x] Неделя 2: Управление потоком (if/for/while), функции
  - [x] Day 1 — Functions & Arguments (`sum_all`, `print_info`, `calc_avg`)
  - [x] Day 2 — Lambda, Map, Filter, Reduce (`squares`, `filter_even`, `product`)
  - [x] Day 3 — Classes & Objects (`Person`, `Circle`, `Book`)
  - [x] Day 4 — Inheritance & Polymorphism (`Animal`, `Dog`, `Cat`, `Account`, `SavingsAccount`)
  - [x] Day 5 — Modules & Imports (`random_sqrt`, `current_date`, `from_math_utils`)
  - [x] Day 6 — Combined Tasks (`Stats`, `sort_and_filter`, `count_letters_in_file`)
  - [x] Day 7 — Mini-project: CLI Calculator 
- [ ] Неделя 3: Исключения, файлы и стандартные модули
  - [x] Day 1 — Exception Handling (`divide`, `safe_int`, `access_list_element`)
  - [x] Day 2 — Custom Exceptions (`NegativeValueError`, `InvalidAgeError`, `check_age`)
  - [x] Day 3 — File Operations (`read_file`, `write_file`, `append_line`)
  - [ ] Day 4 — Pathlib & File Paths (`list_files`, `create_folder`, `file_info`)
  - [ ] Day 5 — Standard Modules (`current_time`, `combine_lists`, `multiply_all`)
  - [ ] Day 6 — Combined Tasks (`read_json`, `count_lines_with_word`, `safe_write`)
  - [ ] Day 7 — Mini-project: Log Analyzer CLI

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