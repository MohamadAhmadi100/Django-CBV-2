from django import forms
from .models import Comment


class AddTodoForm(forms.Form):
    title = forms.CharField(label='', max_length=200, widget=forms.TextInput(
        attrs={'placeholder': 'Todo Title', 'class': 'form form-control col-md-11 m-2'}))


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('title', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'mx-2', 'placeholder': 'title'}),
            'body': forms.Textarea(attrs={'rows': 1, 'cols': '60', 'class': 'mx-2', 'placeholder': ' your comment',
                                          'style': 'resize:none;'}),
        }
        labels = {
            "title": '',
            'body': '',
        }
