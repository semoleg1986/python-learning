.PHONY: requirements install test format lint type-check check help

# ========================
# Requirements
# ========================

requirements: ## Скомпилировать requirements.in в requirements.txt
	pip-compile requirements.in

install: requirements ## Установить зависимости из requirements.txt
	pip install -r requirements.txt

# ========================
# Test
# ========================

test: ## Запустить все тесты
	pytest -v

# ========================
# Code Quality
# ========================

format: ## Автоформатирование кода (black + isort)
	black .
	isort .

lint: ## Линтинг кода (flake8)
	flake8 .

type-check: ## Проверка типов (mypy)
	mypy .

check: format lint type-check ## Запустить все проверки качества кода
	@echo "✅ Все проверки пройдены"

# ========================
# Help
# ========================

help: ## Показать список доступных команд
	@echo "Доступные команды:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| sort \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'