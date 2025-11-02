#!/usr/bin/env bash

# Установка зависимостей
pip install fastapi uvicorn

# Запуск сервиса
uvicorn main:app --reload
