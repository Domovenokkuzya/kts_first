from typing import Optional

__all__ = (
    'find_shortest_longest_word',
)


def find_shortest_longest_word(text: str) -> tuple[Optional[str], Optional[str]]:
    """
    В переданном тексте вернуть слово имеющее наименьшую и наибольшую длину.
    Если такого слова нет - вернуть None
    """
    result: tuple = (None, None)
    word: str = ""
    short: str = ""
    long: str = ""
    text += " "
    for i in text:
        if ("a" <= i <= "z") or ("а" <= i <= "я"):
            word += i
        else:
            if short == "":
                short = word
            if len(word) < len(short) and word != "":
                short = word
            if len(word) > len(long):
                long = word
            word = ""

    if short != "":
        result = (short, long)
    return result
    raise NotImplementedError

find_shortest_longest_word('hello\n\n\tsir')
