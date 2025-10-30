#!/bin/bash
# Практика Git Day 1

# 1. Создаём тестовый проект
mkdir week4/day1_git_basics/git_practice && cd week4/day1_git_basics/git_practice

git init

# 2. Добавляем файлы
echo "print('Hello, Git')" > main.py
git add main.py
git commit -m "feat: add main.py"

#3. Внесем изменение
echo "print('Hello, user')" >> main.py
git diff
git add main.py
git commit -m "feat: updated main.py"

# 4. Проверяем историю
git log --oneline

# 4c095f4 (HEAD -> main) feat: updated main.py
# 03950f4 feat: add main.py

# -> Good

