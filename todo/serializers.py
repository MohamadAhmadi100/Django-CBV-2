from rest_framework import serializers
from .models import Todo, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'title', 'created', 'body')


class TodoSerializer(serializers.ModelSerializer):
    t_comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Todo
        fields = ('id', 'title', 'created', 'slug', 't_comments')
