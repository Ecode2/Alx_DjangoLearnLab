from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import Post, Comment

# TagWidget()", "widgets.SelectMultiple(attrs={"class": "form-control"})
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields=["content"]

class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]