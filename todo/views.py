from .models import Todo, Comment
from django.views.generic import ListView, DetailView, FormView, DeleteView, UpdateView
from django.views.generic.edit import FormMixin
from .forms import AddTodoForm, AddCommentForm
from django.urls import reverse, reverse_lazy
from django.utils.text import slugify
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class TodoDetailView(LoginRequiredMixin, FormMixin, DetailView):
    model = Todo
    template_name = 'todo/todo_detail.html'
    context_object_name = 'todo'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    form_class = AddCommentForm

    def get_success_url(self):
        return reverse('todo:todo_detail', kwargs={'slug': self.object.slug})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            comment = Comment(title=form.cleaned_data['title'], body=form.cleaned_data['body'], todo=self.object)
            comment.save()
        return super().form_valid(form)


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


class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'todo/todo_delete.html'
    success_url = reverse_lazy('todo:home')


class TodoUpdateView(UpdateView):
    model = Todo
    template_name = 'todo/todo_update.html'
    fields = ('title',)
    success_url = reverse_lazy('todo:home')
