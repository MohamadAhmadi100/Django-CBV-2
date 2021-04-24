from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('register/', views.SignUpView.as_view(), name='user_signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='user_logout'),
    path('rest-password/', views.UserPasswordReset.as_view(), name='reset_password'),
    path('reset-done/', views.PasswordResetDone.as_view(), name='password_reset_done'),
    path('reset-confirm/<uidb64>/<token>', views.PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('reset-complete/', views.PasswordResetComplete.as_view(), name='password_reset_complete'),
]
