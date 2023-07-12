from django.contrib.auth import views as auth_views
from .forms import UserRegisterForm
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/user_login.html'


class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'accounts/register.html'
    form_class = UserRegisterForm
    success_message = "Your account was created successfully"
    success_url = reverse_lazy('accounts:user_login')


class UserPasswordReset(auth_views.PasswordResetView):
    template_name = 'accounts/password_reset_form.html'
    success_url = reverse_lazy('accounts:password_reset_done')
    email_template_name = 'accounts/password_reset_email.html'


class PasswordResetDone(auth_views.PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'


class PasswordResetConfirm(auth_views.PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:password_reset_complete')


class PasswordResetComplete(auth_views.PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'
