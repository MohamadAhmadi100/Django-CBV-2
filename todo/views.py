from .models import Todo
from django.views.generic import ListView, DetailView, FormView
from .forms import AddTodoForm
from django.urls import reverse, reverse_lazy
from django.utils.text import slugify
from django.contrib import messages


class TodoDetailView(DetailView):
    model = Todo
    template_name = 'todo/todo_detail.html'
    context_object_name = 'todo'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class TodoListView(FormView, ListView):
    model = Todo
    template_name = 'todo/home.html'
    ordering = ['-created']
    context_object_name = 'todos'
    form_class = AddTodoForm
    success_url = reverse_lazy('todo:home')

    def form_valid(self, form):
        self.create_todo(form.cleaned_data)
        return super().form_valid(form)

    def create_todo(self, data):
        todo = Todo(title=data['title'], slug=slugify(data['title']))
        todo.save()
        messages.success(self.request, 'Todo added successfully', 'success')
