from django.contrib.auth import views as auth_views
from django.urls import path

from . import views, api_views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('register/', views.SignUpView.as_view(), name='user_signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='user_logout'),
    path('rest-password/', views.UserPasswordReset.as_view(), name='reset_password'),
    path('reset-done/', views.PasswordResetDone.as_view(), name='password_reset_done'),
    path('reset-confirm/<uidb64>/<token>', views.PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('reset-complete/', views.PasswordResetComplete.as_view(), name='password_reset_complete'),
    path('api/login/', api_views.LoginAPIView.as_view(), name='login'),
    path('api/users/', api_views.UserListCreateAPIView.as_view(), name='user-list'),
    path('api/users/<int:pk>/', api_views.UserDetailAPIView.as_view(), name='user-detail'),
    path('register/', api_views.RegisterView.as_view(), name='register'),
]
