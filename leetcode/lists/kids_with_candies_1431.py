def kids_with_candies(candies: list[int], extra: int) -> list[bool]:
    """
    Определяет, смогут ли дети получить наибольшее количество конфет,
    если каждому добавить extra конфет.

    :param candies: Список целых чисел.
    :type candies: list[int]
    :param extra: Количество дополнительных конфет.
    :type extra: int
    :return: Список булевых значений
    :rtype: list[bool]
    """
    max_item = max(candies)
    result = [i + extra >= max_item for i in candies]
    return result
