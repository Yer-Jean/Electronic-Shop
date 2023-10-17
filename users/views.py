import random
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.utils.crypto import get_random_string
from django.views.generic import CreateView

from users.forms import UserRegisterForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm  # Переопределяем стандартную форму UserCreationForm на свою
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        self.object = form.save()
        self.object.verification_token = get_random_string(30)
        send_mail(
            subject='Activate Your Account Now',
            message=f'Hello!\nPlease, click link below to confirm your email\n'
                    f'http://{get_current_site(self.request)}/users/confirm/{self.object.verification_token}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.object.email]
        )
        return super().form_valid(form)


def activate_user(request, token):
    user = User.objects.get(verification_token=token)
    user.verification_token = ''
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


def reset_password(request):
    context = {
        'title': 'Resetting Password',
        'sub_title': 'You will receive a new password to the specified email'
    }

    if request.method == 'POST':
        # Проверка на существование введенного email в БД
        try:
            user = User.objects.get(email=request.POST.get('email'))
        except User.DoesNotExist:
            context = {
                'title': 'User with this email does not exist',
                'sub_title': 'Try entering the email again'
            }
            return render(request, 'users/pass_reset.html', context)
        # Генерируем пароль из 12-ти случайных цифр
        new_password = ''.join([str(random.randint(0, 9)) for _ in range(12)])
        # Отправляем пароль по email пользователю
        send_mail(
            subject='New password',
            message=f'Hello!\nThis is your new password: {new_password}\n\nDo not tell it to anyone.',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        # Записываем в БД новый пароль
        user.set_password(new_password)
        user.save()
        # После отправки письма с паролем переходим на страницу авторизации
        return redirect(reverse_lazy('users:login'))
    return render(request, 'users/pass_reset.html', context)
