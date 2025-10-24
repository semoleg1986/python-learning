#!/bin/bash
# Практика Git Day 2

# 1. Создаём тестовый проект
mkdir week4/day2_branches_remote/git_practice && cd week4/day2_branches_remote/git_practice

git init

# 2. Добавляем файлы
echo "print('Hello, Git')" > day1.py
git add day1.py
git commit -m "feat: add day1.py"

# 3. Создаем ветку
git checkout -b feature/day2

# 4. Вносим изменения и сделаем коммит
echo "print('Git Day 2')" > day2.py
git add .
git commit -m "feat: add day2.py"

# 5. Сделаем слияние в main
git switch main
git merge feature/day2

# 6. Проверим logs
git log --oneline

# [main (root-commit) 6ff328e] feat: add day1.py
#  1 file changed, 1 insertion(+)
#  create mode 100644 day1.py
# Switched to a new branch 'feature/day2'
# [feature/day2 7324452] feat: add day2.py
#  1 file changed, 1 insertion(+)
#  create mode 100644 day2.py
# Switched to branch 'main'
# Updating 6ff328e..7324452
# Fast-forward
#  day2.py | 1 +
#  1 file changed, 1 insertion(+)
#  create mode 100644 day2.py
# 7324452 (HEAD -> main, feature/day2) feat: add day2.py
# 6ff328e feat: add day1.py

# -> Good
