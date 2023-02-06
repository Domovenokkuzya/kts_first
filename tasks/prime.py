__all__ = (
    'is_prime',
)


def is_prime(number: int) -> bool:
    """
    Функция должна вернуть True если число является простым, иначе - False
    """
    if (number > 3 and (number % 2 == 0 or number % 3 == 0)) or number == 0 or number == 1:
        return False
    else:
        return True

    raise NotImplementedError
