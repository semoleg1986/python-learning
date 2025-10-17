#!/usr/bin/env python3
from cli import App


def main() -> None:
    """
    Точка входа в программу Word Analyzer CLI.

    Запускает CLI приложение для анализа текста:
      • подсчёт слов;
      • подсчёт уникальных слов;
      • топ-5 самых частых слов.
    """
    app = App()
    app.run()


if __name__ == "__main__":
    main()
