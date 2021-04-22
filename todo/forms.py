from django import forms


class AddTodoForm(forms.Form):
    title = forms.CharField(label='', max_length=200, widget=forms.TextInput(
        attrs={'placeholder': 'Todo Title', 'class': 'form form-control col-md-11 m-2'}))
