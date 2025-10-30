# 🔹 День 4 — Работа с .gitignore и безопасностью

## 🧠 Теория

### Что нельзя коммитить в репозиторий

Никогда не загружай в публичный репозиторий файлы, содержащие:
- ключи API, токены, пароли
- .env (переменные окружения)
- виртуальное окружение (.venv/)
- системные файлы IDE (.idea/, .vscode/)
- скомпилированные файлы (__pycache__/, *.pyc)
- файлы зависимостей, если есть requirements.txt (node_modules/, venv/)

### Файл .gitignore

.gitignore сообщает Git, какие файлы и папки не нужно отслеживать.
Пример .gitignore для Python-проектов:

```commandline
# Виртуальное окружение
.venv/

# Кэш Python
__pycache__/
*.py[cod]

# Конфигурации IDE
.vscode/
.idea/

# Логи
*.log

# Секреты
.env

# Тестовые файлы
*.pytest_cache/
.coverage
```

Совет: готовые шаблоны можно взять на
https://github.com/github/gitignore

### SSH-ключи для GitHub

SSH позволяет подключаться к GitHub без логина и пароля.

1. Создание ключа:
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```
2. Добавление ключа в ssh-agent:
```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```
3. Добавление публичного ключа на GitHub:

- Скопируй содержимое файла:
```commandline
cat ~/.ssh/id_ed25519.pub
```
- Перейди в
```note
 GitHub → Settings → SSH and GPG keys → New SSH key
```
- Вставь ключ и сохрани.

