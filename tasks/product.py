from typing import Any

__all__ = (
    'cartesian_product',
)


def cartesian_product(arr1: list[Any], arr2: list[Any]) -> list:
    """
    Должна возвращать все пары элементы двух массивов:
    cartesian_product([1, 2], [3, 4]) == [(1, 3), (1, 4), (2, 3), (2, 4)]
    """
    if not arr1 or not arr2:
        return list()
    combinations_quantity: int = len(arr1) * len(arr2)
    arr: list[tuple] = []
    combination: tuple[Any] = ()
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            combination = (arr1[i], arr2[j])
            arr.append(combination)
    return arr
    raise NotImplementedError
