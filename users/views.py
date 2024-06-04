import secrets
import random
import string

from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, FormView
from django.contrib.auth.hashers import make_password

from users.forms import UserRegisterForm, PasswordResetRequestForm
from users.models import User

from config.settings import EMAIL_HOST_USER


class RegisterUserView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f"http://{host}/users/email_confirm/{token}/"
        send_mail(
            subject="Подтверждение регистрации",
            message=f"Для подтверждения регистрации перейдите по ссылке: {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))


class ChangePasswordView(FormView):
    template_name = 'users/change_password.html'
    form_class = PasswordResetRequestForm
    success_url = reverse_lazy("users:login")  # URL куда перенаправить после успешного восстановления пароля

    def form_valid(self, form):
        email = form.cleaned_data['email']
        try:
            user = User.objects.get(email=email)
            new_password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
            user.password = make_password(new_password)
            user.save()
            send_mail(
                subject='Ваш новый пароль',
                message=f'Ваш новый пароль: {new_password}',
                from_email=EMAIL_HOST_USER,  # Замените на ваш email
                recipient_list=[user.email]
            )
        except User.DoesNotExist:
            form.add_error('email', 'Пользователь с таким email не найден')
            return self.form_invalid(form)

        return super().form_valid(form)
