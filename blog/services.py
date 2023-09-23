from django.conf import settings
from django.core.mail import send_mail

from blog.models import Article


def send_greeting_email(order_item: Article):
    send_mail(
        'Поздравляем! У тебя 100 просмотров!',
        f'Статья "{order_item.title}" набрала 100 просмотров.',
        settings.EMAIL_HOST_USER,
        ['yerg@mac.com']
    )
