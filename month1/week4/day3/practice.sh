#!/bin/bash
# Практика Git Day 3

# 1. Создай ветку:
git checkout -b feature/day3

# 2. Внеси изменения и закоммить:
git add .
git commit -m "feat: добавил обработку ошибок"
git push origin feature/day3

# 3. Создай Pull Request на GitHub (из feature/day3 → main).

# 4. Отправь ссылку на PR на ревью.

# 5. После одобрения — выполни merge:
#	•	через GitHub (кнопка Merge pull request),
#	•	или локально:

git checkout main
git pull origin main
git merge feature/day3
git push origin main