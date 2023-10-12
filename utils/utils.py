import string


def text_to_set_without_punctuation(text: str) -> set:
    """Метод удаляя знаки препинания из строки text,
    затем разбивает эту строку на множество слов из которых
    она состоит, и возвращает это множество"""
    if text:
        text = text.translate(str.maketrans('', '', string.punctuation)).lower()
        return set(text.split())
    return None
