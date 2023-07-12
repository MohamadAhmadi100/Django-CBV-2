from django.urls import path
from . import views
from . import api_views

app_name = 'todo'
urlpatterns = [
    path('', views.TodoListView.as_view(), name='home'),
    path('update/<int:pk>', views.TodoUpdateView.as_view(), name='update_todo'),
    path('delete/<int:pk>/', views.TodoDeleteView.as_view(), name='delete_todo'),
    path('<slug:slug>/', views.TodoDetailView.as_view(), name='todo_detail'),
    path('api/todos/', api_views.TodoListAPIView.as_view(), name='todo-list-create'),
    path('api/todos/<int:pk>/', api_views.TodoDetailAPIView.as_view(), name='todo-detail'),
    path('api/comments/', api_views.CommentListAPIView.as_view(), name='comment-list-create'),
    path('api/comments/<int:pk>/', api_views.CommentDetailAPIView.as_view(), name='comment-detail'),
]
