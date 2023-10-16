import string

from django.core.mail import send_mail

from django.conf import settings

from blog.models import Article


def text_to_set_without_punctuation(text: str) -> set:
    """Метод удаляя знаки препинания из строки text,
    затем разбивает эту строку на множество слов из которых
    она состоит, и возвращает это множество"""
    if text:
        text = text.translate(str.maketrans('', '', string.punctuation)).lower()
        return set(text.split())
    return None


def send_greeting_email(order_item: Article):
    send_mail(
        'Поздравляем! У тебя 100 просмотров!',
        f'Статья "{order_item.title}" набрала 100 просмотров.',
        settings.EMAIL_HOST_USER,
        ['yerg@mac.com']
    )