from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.TodoListView.as_view(), name='home'),
    path('update/<int:pk>', views.TodoUpdateView.as_view(), name='update_todo'),
    path('delete/<int:pk>/', views.TodoDeleteView.as_view(), name='delete_todo'),
    path('<slug:slug>/', views.TodoDetailView.as_view(), name='todo_detail'),
]
