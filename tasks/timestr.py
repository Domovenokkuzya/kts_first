__all__ = (
    'seconds_to_str',
)


def seconds_to_str(seconds: int) -> str:
    """
    Функция должна вернуть текстовое представление времени
    20 -> 20s
    60 -> 01m00s
    65 -> 01m05s
    3700 -> 01h01m40s
    93600 -> 01d02h00m00s
    """

    minutes: int = 0
    hours: int = 0
    days: int = 0

    time: str = ""

    while seconds > 86359:
        seconds -= 86400
        days += 1

    if days > 0:
        if days > 9:
            time += str(days)
        else:
            time += "0"
            time += str(days)
        time += "d"

    while seconds > 3599:
        seconds -= 3600
        hours += 1

    if hours > 0 or days > 0:
        if hours > 9:
            time += str(hours)
        else:
            time += "0"
            time += str(hours)
        time += "h"

    while seconds > 59:
        seconds -= 60
        minutes += 1

    if minutes > 0 or hours > 0 or days > 0:
        if minutes > 9:
            time += str(minutes)
        else:
            time += "0"
            time += str(minutes)
        time += "m"

    if seconds > 9:
        time += str(seconds)
    else:
        time += "0"
        time += str(seconds)
    time += "s"

    return time

    raise NotImplementedError




