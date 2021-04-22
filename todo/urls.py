from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.TodoListView.as_view(), name='home'),
    path('delete/<int:pk>/', views.TodeDeleteView.as_view(), name='delete_tode'),
    path('<slug:slug>/', views.TodoDetailView.as_view(), name='todo_detail'),
]
