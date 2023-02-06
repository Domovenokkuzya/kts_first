__all__ = (
    'even_odd',
)


def even_odd(arr: list[int]) -> float:
    """
    Функция возвращает отношение суммы четных элементов массив к сумме нечетных
    Пример:
    even_odd([1, 2, 3, 4, 5]) == 0,6667
    """
    nechet: int = 0
    chet: int = 0
    for i in arr:
        if i % 2 == 0:
            chet += i
        else:
            nechet += i
    if nechet == 0:
        return 0
    return float(chet/nechet)
    raise NotImplementedError
