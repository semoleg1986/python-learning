def can_place_flowers(flowerbed: list[int], n: int) -> bool:
    """
    Определяет, можно ли посадить `n` новых цветов в клумбу,
    не нарушая правило, что цветы не могут расти на соседних участках.

    :param flowerbed: Список, представляющий клумбу (0 — пусто, 1 — занято).
    :type flowerbed: list[int]
    :param n: Количество цветов, которые нужно посадить.
    :type n: int
    :return: True, если можно посадить n цветов, иначе False.
    :rtype: bool
    """
    if n == 0:
        return True

    bed = [0] + flowerbed + [0]
    count = 0

    for i in range(1, len(bed) - 1):
        if bed[i - 1] == bed[i] == bed[i + 1] == 0:
            bed[i] = 1
            count += 1
            if count >= n:
                return True

    return False


if __name__ == "__main__":
    print(can_place_flowers([1, 0, 0, 0, 1], 1))  # 5 3 1 нужен 3
    print(can_place_flowers([1, 0, 0, 0, 1], 2))  # 5 3 2 нужен 4
    print(can_place_flowers([0, 0, 1, 0, 0], 2))  # 5 4 2 нужен 4
    print(can_place_flowers([1, 0, 0, 0, 0, 1], 1))  # 6 4 1 нужен 3
    print(can_place_flowers([1, 0, 0, 0, 0, 1], 2))  # 6 4 2  нужен 5
    print(can_place_flowers([1, 0, 0, 0, 0, 0, 1], 3))  # 7 5 3 нужен 7
    print(can_place_flowers([1, 0, 0, 0, 0, 0, 1], 2))  # 7 5 2 нужен 5
