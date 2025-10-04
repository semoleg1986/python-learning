from analyzer import Analyser
from tabulate import tabulate

instruction = """
Программа запушена

Команды:

start - запуск
exit  - выход
"""


class App:
    def __init__(self) -> None:
        """
        Инициализирует приложение и устанавливает состояние цикла.
        """
        self.running = True
        self.columns = ("Qnty words", "Qnty uniq words", "Top 5 words")

    def run(self) -> None:
        """
        Запускает основной цикл программы.

        Ожидает команды пользователя:
          • 'start' — запустить анализ текста;
          • 'exit' — завершить программу.
        """
        while self.running:
            command = input(instruction + "\nВведите команду: ").strip().lower()
            if command == "start":
                self.start()
            elif command == "exit":
                self.exit()
            else:
                print("Неизвестная команда\n")

    def start(self) -> None:
        """
        Запускает процесс анализа текста.
        """
        print("Введите текст (одной строкой):")
        text = input("> ").strip()
        analyzer = Analyser(text)
        table = [
            (
                analyzer.count_words(),
                analyzer.count_uniq_words(),
                ", ".join(analyzer.top_freq_words()),
            )
        ]
        print(tabulate(table, headers=self.columns, tablefmt="grid"))

    def exit(self) -> None:
        """
        Завершает выполнение программы.
        """
        print("Программа закрыта")
        self.running = False
