#!/bin/bash
# Практика Git Day 4

# 1. Создай .gitignore в корне проекта:
touch .gitignore

# 2. Добавь в него:
echo ".venv/" >> .gitignore
echo "__pycache__/" >> .gitignore
echo ".env" >> .gitignore

# 3. Убедись, что эти файлы не будут добавлены:
git status

# 4. Настрой SSH:
ssh-keygen -t ed25519 -C "your_email@example.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# 5, Добавь ключ в GitHub (Settings → SSH Keys) и проверь соединение:
ssh -T git@github.com