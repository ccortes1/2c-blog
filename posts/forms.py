""" Post forms """

# Django
from django import forms

# Models
from posts.models import Post, Category, Comment

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'text_body', 'pub_date']
        widgets = {
            'pub_date': DateTimeInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text',]
