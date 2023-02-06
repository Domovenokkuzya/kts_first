from typing import Any

__all__ = (
    'corresponding_pairs',
)


def corresponding_pairs(arr1: list[Any], arr2: list[Any]) -> list[tuple[Any, Any]]:
    """
    Функция должна возвращать соответствующие элементы двух массивов:
    corresponding_pairs([1, 2], [3, 4]) == [(1, 3), (2, 4)]
    """
    if not arr1 or not arr2:
        return list()
    a: Any = arr1[0]
    arr1[0] = arr2[1]
    arr2[0] = a
    return list[tuple(arr1, arr2)]

    raise NotImplementedError
