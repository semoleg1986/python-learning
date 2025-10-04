import argparse

from analyzer import Analyser
from tabulate import tabulate
from utils.logger import get_logger

logger = get_logger(__name__)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Word Analyzer CLI")
    parser.add_argument("--file", help="Путь к файлу с текстом")
    parser.add_argument("--top", type=int, default=5, help="Количество слов в топе")
    return parser.parse_args()


class App:
    """
    CLI-приложение
    """

    def __init__(self) -> None:
        self.columns = ("Words", "Unique", "Top words")

    def run(self) -> None:
        """
        Точка входа CLI. Обрабатывает аргументы.
        """
        args = parse_args()
        if args.file:
            try:
                with open(args.file, "r", encoding="utf-8") as f:
                    text = f.read()
            except FileNotFoundError:
                logger.error(f"Файл `{args.file}` не найден")
                print(f"Ошибка: файл '{args.file}' не найден.")
                return
        else:
            text = input("> ")
        self.start(text, args.top)

    def start(self, text: str, top_n: int) -> None:
        """
        Запускает процесс анализа текста.

        :param text: Входной текст для анализа.
        :type text: str
        :param top_n: Количество слов в топе.
        :type top_n: int
        """
        analyzer = Analyser(text)
        table = [
            (
                analyzer.count_words(),
                analyzer.count_uniq_words(),
                ", ".join(analyzer.top_freq_words(top_n)),
            )
        ]
        print(tabulate(table, headers=self.columns, tablefmt="grid"))
        logger.info("Анализ успешно завершён")
