from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(max_length=200)
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name='t_comments')

    def __str__(self):
        return self.title
