#!/usr/bin/env python3
"""
Точка входа в программу Word Analyzer CLI.

Запускает CLI приложение для анализа текста:
  • подсчёт слов;
  • подсчёт уникальных слов;
  • топ-5 самых частых слов.
"""

from cli import App

if __name__ == "__main__":
    app = App()
    app.run()
