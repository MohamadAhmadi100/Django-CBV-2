from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.TodoListView.as_view(), name='home'),
    path('<slug:slug>/', views.TodoDetailView.as_view(), name='todo_detail'),
]
