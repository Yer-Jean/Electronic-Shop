from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='yerg@mac.com',
            first_name='Yerg',
            last_name='Mac',
            is_staff=True,
            is_superuser=True
        )
        user.set_password('15679')
        user.save()
