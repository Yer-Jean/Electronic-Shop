from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import UserRegisterForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm  # Переопределяем стандартную форму UserCreationForm на свою
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')
